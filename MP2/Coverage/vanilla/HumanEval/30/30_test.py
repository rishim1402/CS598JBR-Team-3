import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.30.function')
get_positive = module.get_positive

import pytest