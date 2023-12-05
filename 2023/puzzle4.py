# Imports

# Vanilla Python Modules

import math
import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day02_test.txt"
TEST_ANSWER = 2286
PUZZLE_DATA = "./data/day02.txt"

DATA_REG_EXP = r"(?:\s)([0-9]+)(?:\s)([a-z]+)"


# Private Functions

@utils.test_puzzle(TEST_DATA, TEST_ANSWER)
def _calculate(input_path):
    """Calculate the result from the given input data.
    
    Args:
        input_path (str): Path to a file containing the input data to process.
        
    Returns:
        str | int
    """
    _result = 0
    _text = utils.read_doc(input_path=input_path)
    for _line in _text:
        _maxes = {}
        for _count, _color in re.findall(DATA_REG_EXP, _line):
            _maxes[_color] = max(_maxes.setdefault(_color, 0), int(_count))
        _result += math.prod(_maxes.values())
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

