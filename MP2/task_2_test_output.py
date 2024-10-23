import jsonlines
import sys
import torch
import os
import re
import subprocess
import json
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

#####################################################
# Please finish all TODOs in this file for MP2;
#####################################################

def save_file(content, file_path):
    with open(file_path, 'a') as file:
        file.write(content)

# def extract_and_fix_test_cases(generated_code, function_name, id, prompt_type_folder):
#     # Extract the code between <START_TESTS> and <END_TESTS> tokens
#     match = re.search(r'<START_TESTS>(.*?)<END_TESTS>', generated_code, re.DOTALL)
#     if not match:
#         print("No test cases found between <START_TESTS> and <END_TESTS> tokens.")
#         return ""

#     test_cases = match.group(1).strip()
#     print(test_cases)

#     # Remove any 'from <module> import <function>' or 'import <module>'
#     test_cases = re.sub(r"from\s+\S+\s+import\s+\S+", "", test_cases)  # Remove 'from x import y'
#     test_cases = re.sub(r"import\s+\S+", "", test_cases)  # Remove 'import x'

#     # Ensure 'pytest' is imported
#     if "import pytest" not in test_cases:
#         test_cases = "import pytest\n\n" + test_cases

#     # Add the correct import statement
#     import_statement = f"import sys\nsys.path.append('/content/CS598JBR-Team-3/MP2')\nimport importlib\nmodule = importlib.import_module('Coverage.{prompt_type_folder}.HumanEval.{id}.function')\n{function_name} = module.{function_name}"

#     if import_statement not in test_cases:
#         test_cases = import_statement + "\n\n" + test_cases

#     # Clean up any extra blank lines caused by removing imports
#     test_cases = re.sub(r'\n\s*\n', '\n\n', test_cases).strip()

#     return test_cases


def run_pytest_and_get_coverage(task_id, prompt_type):
    # Define the pytest command
    id  = task_id.split('/')[1]
    pytest_command = [
        'pytest', f'Coverage/{prompt_type}/HumanEval/{id}/{id}_test.py'
    ]

    # Run pytest using subprocess
    result = subprocess.run(pytest_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if pytest ran successfully
    # if result.returncode != 0:
    #     print("Error running pytest:")
    #     print(result.stderr.decode('utf-8'))
    #     return None

    # Path to the generated coverage report
    print(result)


def prompt_model(dataset, vanilla = True):
    print(f"Working with  prompt type {vanilla}...")

    # Download and load the model with quantization
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype=torch.bfloat16
    # )
    # model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config, device_map="auto")
    # tokenizer = AutoTokenizer.from_pretrained(model_name)

    results = []
    for entry in dataset:
        prompt_type_folder = ""
        if vanilla:
            prompt_type_folder = "vanilla"
        #     prompt = entry.get('prompt', '')
        #     canonical_solution = entry.get('canonical_solution', '')
        #     function_definition = prompt + canonical_solution
        #     prompt = f"You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.\n### Instruction:\nGenerate a pytest test suite for the following code.\nOnly write unit tests between the tokens `<START_TESTS>` and `<END_TESTS>`\n . The function is provided below: Function definition: \n {function_definition}"
        else:
            prompt_type_folder = "crafted"
        #     prompt = entry.get('prompt', '')
        #     canonical_solution = entry.get('canonical_solution', '')
        #     function_definition = prompt + canonical_solution
        #     prompt = f"Generate `pytest` test cases for the following Python function. Only include the pytest test functions between the tokens `<START_TESTS>` and `<END_TESTS>`.\n The function is provided below: Function definition: \n {function_definition}"

        # # TODO: prompt the model and get the response
        # input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        # output = model.generate(input_ids, max_length=2000, num_return_sequences=1, temperature=0)
        # prompt_length = len(input_ids[0])
        # response = tokenizer.decode(output[0][prompt_length:], skip_special_tokens=True)

        # #extract the signature from promt and code from cannonical solution and write it to a file
        # directory = f"./Coverage/{prompt_type_folder}/{entry['task_id']}"
        # filename = f"function.py"
        # os.makedirs(directory, exist_ok=True)
        # file_path = os.path.join(directory, filename)
        # with open(file_path, "w") as file:
        #     file.write(function_definition)

        # print(f"Function definition written to {file_path}")


        # #add import statement to response
        # match = re.search(r'def\s+([a-zA-Z_]\w*)\s*\(', entry["prompt"])
        # function_name = match.group(1)
        # id = entry['task_id'].split('/')[1]
        # modified_response = extract_and_fix_test_cases(response, function_name, id, prompt_type_folder)


        # #write the generated response to a py file
        # testname = f"{id}_test.py"
        # file_path = os.path.join(directory, testname)
        # with open(file_path, "w") as file:
        #     file.write(modified_response)

        # print(f"Test written to {file_path}")

        # #generate coverage

        # # TODO: process the response, generate coverage and save it to results
        coverage = run_pytest_and_get_coverage(entry['task_id'], prompt_type_folder)

        # print(f"Task_ID {entry['task_id']}:\nprompt:\n{prompt}\nresponse:\n{response}\ncoverage:\n{coverage}")
        #print(f"Task_ID {entry['task_id']}")
        #print(f"{modified_response}")
        # results.append({
        #     "task_id": entry["task_id"],
        #     "prompt": prompt,
        #     "response": response,
        #     "coverage": f"{coverage}%"
        # })

    return results

def read_jsonl(file_path):
    dataset = []
    with jsonlines.open(file_path) as reader:
        for line in reader:
            dataset.append(line)
    return dataset

def write_jsonl(results, file_path):
    with jsonlines.open(file_path, "w") as f:
        for item in results:
            f.write_all([item])

if __name__ == "__main__":
    """
    This Python script is to run prompt LLMs for code synthesis.
    Usage:
    `python3 task_2.py <input_dataset> <model> <output_file> <if_vanilla>`|& tee prompt.log

    Inputs:
    - <input_dataset>: A `.jsonl` file, which should be your team's dataset containing 20 HumanEval problems.
    - <model>: Specify the model to use. Options are "deepseek-ai/deepseek-coder-6.7b-base" or "deepseek-ai/deepseek-coder-6.7b-instruct".
    - <output_file>: A `.jsonl` file where the results will be saved.
    - <if_vanilla>: Set to 'True' or 'False' to enable vanilla prompt

    Outputs:
    - You can check <output_file> for detailed information.
    """
    args = sys.argv[1:]
    input_dataset = args[0]
    # model = args[1]
    output_file = args[1]
    if_vanilla = args[2] # True or False

    if not input_dataset.endswith(".jsonl"):
        raise ValueError(f"{input_dataset} should be a `.jsonl` file!")

    if not output_file.endswith(".jsonl"):
        raise ValueError(f"{output_file} should be a `.jsonl` file!")

    vanilla = True if if_vanilla == "True" else False

    dataset = read_jsonl(input_dataset)
    results = prompt_model(dataset, vanilla)
    # write_jsonl(results, output_file)
