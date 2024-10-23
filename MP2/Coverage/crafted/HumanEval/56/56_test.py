import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.56.function')
correct_bracketing = module.correct_bracketing

import pytest

def test_correct_bracketing():
    assert correct_bracketing("<") == False
    assert correct_bracketing("<>") == True
    assert correct_bracketing("<<><>>") == True
    assert correct_bracketing("><<>") == False