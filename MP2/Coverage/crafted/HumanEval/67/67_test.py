import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.67.function')
fruit_distribution = module.fruit_distribution

import pytest

def test_fruit_distribution():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges",3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges",120) == 19