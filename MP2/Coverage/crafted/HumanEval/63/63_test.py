import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.63.function')
fibfib = module.fibfib

import pytest

def test_fibfib():
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 84
    assert fibfib(15) == 303
    assert fibfib(20) == 976