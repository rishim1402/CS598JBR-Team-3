import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.21.function')
rescale_to_unit = module.rescale_to_unit

import pytest

def test_rescale_to_unit():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([-1.0, 1.0]) == [0.0, 1.0]
    assert rescale_to_unit([0.0]) == [0.0]
    assert rescalecale_to_unit([1.0, 1.0, 1.0]) == [0.5, 0.5, 0.5]