import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.crafted.HumanEval.81.function')
numerical_letter_grade = module.numerical_letter_grade

import pytest

def test_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    assert numerical_letter_grade([0.0]) == ['E']
    assert numerical_letter_grade([4.0]) == ['A+']
    assert numerical_letter_grade([3.7]) == ['A']
    assert numerical_letter_grade([3.3]) == ['A-']
    assert numerical_letter_grade([3.0]) == ['B+']
    assert numerical_letter_grade([2.7]) == ['B']
    assert numerical_letter_grade([2.3]) == ['B-']
    assert numerical_letter_grade([2.0]) == ['C+']
    assert numerical_letter_grade([1.7]) == ['C']
    assert numerical_letter_grade([1.3]) == ['C-']
    assert numerical_letter_grade([1.0]) == ['D+']
    assert numerical_letter_grade([0.7]) == ['D']
    assert numerical_letter_grade([0.0]) == ['E']