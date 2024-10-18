import jsonlines
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

def save_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

def prompt_model(dataset, model_name = "deepseek-ai/deepseek-coder-6.7b-instruct", vanilla = True):
    print(f"Working with {model_name} prompt type {vanilla}...")
    
    # Download and load the model with quantization
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    results = []
    for entry in dataset:
        # Create prompt for the model based on instructions
        if vanilla:
            try:
                test_assertion = entry['test'].split('assert')[1].strip()
                if 'not candidate' in test_assertion:
                    input_str = test_assertion.split('not candidate(')[1].split(')')[0].strip()
                    expected_output = False
                else:
                    input_str = test_assertion.split('candidate(')[1].split(')')[0].strip()
                    expected_output = test_assertion.split('==')[1].strip()
                
                input_str = input_str.strip("'")  # Remove surrounding single quotes
            except IndexError:
                print(f"Skipping task_id {entry['task_id']} due to unexpected test format")
                continue
            
            prompt = f"You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeekCoder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.\n### Instruction:\nIf the input is '{input_str}', what will the following code return?\nThe return value prediction must be enclosed between [Output] and [/Output] tags. For example: [Output]prediction[/Output].\n```\n{entry['canonical_solution']}\n```\n### Response:"
        else:
            # TODO: Implement prompt crafting as per instructions
            prompt = ""
        
        # Prompt the model and get the response
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        output = model.generate(input_ids, max_length=500, num_return_sequences=1, temperature=0.7)
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Process the response and save it to results
        predicted_output = response.split('[Output]')[1].split('[/Output]')[0].strip() if '[Output]' in response else ""
        verdict = str(predicted_output == str(expected_output))

        print(f"Task_ID {entry['task_id']}:\nprompt:\n{prompt}\nresponse:\n{response}\nis_correct:\n{verdict}")
        results.append({
            "task_id": entry["task_id"], 
            "prompt": prompt,
            "response": response, 
            "is_correct": verdict
        })
        
    return results

def read_jsonl(file_path):
    dataset = []
    with jsonlines.open(file_path) as reader:
        for line in reader: 
            dataset.append(line)
    return dataset

def write_jsonl(results, file_path):
    with jsonlines.open(file_path, "w") as f:
        f.write_all(results)

if __name__ == "__main__":
    args = sys.argv[1:]
    input_dataset = args[0] 
    model = args[1]
    output_file = args[2]
    if_vanilla = args[3] # True or False
    
    if not input_dataset.endswith(".jsonl"):
        raise ValueError(f"{input_dataset} should be a `.jsonl` file!")
    
    if not output_file.endswith(".jsonl"):
        raise ValueError(f"{output_file} should be a `.jsonl` file!")
    
    vanilla = True if if_vanilla == "True" else False
    
    dataset = read_jsonl(input_dataset)
    results = prompt_model(dataset, model, vanilla)
    write_jsonl(results, output_file)
