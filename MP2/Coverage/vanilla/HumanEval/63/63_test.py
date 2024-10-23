import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.63.function')
fibfib = module.fibfib

import pytest

def test_fibfib():
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 8
    assert fibfib(7) == 15
    assert fibfib(8) == 29
    assert fibfib(9) == 56
    assert fibfib(10) == 120