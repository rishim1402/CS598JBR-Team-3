import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.19.function')
sort_numbers = module.sort_numbers

import pytest

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('') == ''
    assert sort_numbers('one one one') == 'one one one'