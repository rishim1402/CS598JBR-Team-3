import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.82.function')
prime_length = module.prime_length

import pytest

def test_prime_length():
    assert prime_length('Hello') == True
    assert prime length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False
    assert prime_length('') == False
    assert prime_length('a') == False