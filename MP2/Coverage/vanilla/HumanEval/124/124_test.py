import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.124.function')
valid_date = module.valid_date

import pytest

def test_valid_date():
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-22012') == False
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False