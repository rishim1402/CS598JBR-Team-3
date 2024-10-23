import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.107.function')
even_odd_palindrome = module.even_odd_palindrome

import pytest

def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(1) == (0, 1)
    assert even_odd_palindrome(1000) == (247, 495)