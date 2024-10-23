import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.29.function')
filter_by_prefix = module.filter_by_prefix

import pytest

def test_filter_by_prefix_empty():
    assert filter_by_prefix([], 'a') == []

def test_filter_by_prefix_single_match():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

def test_filter_by_prefix_multiple_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'aardvark'], 'a') == ['abc', 'array', 'aardvark']

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['bcd', 'cde', 'array'], 'a') == []