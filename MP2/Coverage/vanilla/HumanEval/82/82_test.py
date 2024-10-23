import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.82.function')
prime_length = module.prime_length

import pytest

def test_prime_length():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False
    assert prime_length('') == False
    assert prime_length('a') == False