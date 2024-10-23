import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.27.function')
flip_case = module.flip_case

import pytest

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flipip_case('HELLO') == 'hello'
    assert flip_case('12345') == '12345'
    assert flip_case('') == ''