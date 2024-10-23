import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.0.function')
has_close_elements = module.has_close_elements

import pytest

def test_has_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.7) == False