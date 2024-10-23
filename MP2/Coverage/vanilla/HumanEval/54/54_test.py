import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.54.function')
same_chars = module.same_chars

import pytest

# Write your tests here