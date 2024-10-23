import sys
sys.path.append('/content/CS598JBR-Team-3/MP2')
import importlib
module = importlib.import_module('Coverage.vanilla.HumanEval.21.function')
rescale_to_unit = module.rescale_to_unit

import pytest