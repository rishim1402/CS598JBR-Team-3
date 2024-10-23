import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.56.function')
correct_bracketing = module.correct_bracketing

import pytest