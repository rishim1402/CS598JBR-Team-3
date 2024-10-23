import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.3.function')
below_zero = module.below_zero

import pytest

def test_below_zero():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([1, 2, 3, -5]) == True
    assert below_zero([10, -10, -10, 10]) == False
    assert below_zero([10, 10, -20, 10]) == False
    assert below_zero([10, 10, -30, 10]) == True