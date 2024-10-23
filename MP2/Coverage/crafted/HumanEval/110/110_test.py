import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.110.function')
exchange = module.exchange

import pytest

def test_exchange():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert exchange([2, 2, 2, 2], [1, 1, 1, 1]) == "YES"
    assert exchange([1, 1, 1, 1], [2, 2, 2, 2]) == "NO"