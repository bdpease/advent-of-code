# Imports

# Vanilla Python Modules

import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day02_test.txt"
TEST_ANSWER = 8
PUZZLE_DATA = "./data/day02.txt"

RED = "red"
GREEN = "green"
BLUE = "blue"
LIMITS = {
    RED: 12,
    GREEN: 13,
    BLUE: 14
}
IDX_REG_EXP = r"^(?:Game\s)([0-9]+)"
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
        _index = int(re.match(IDX_REG_EXP, _line).groups()[0])
        _maxes = {}
        for _count, _color in re.findall(DATA_REG_EXP, _line):
            _maxes[_color] = max(_maxes.setdefault(_color, 0), int(_count))
        if all(_max <= LIMITS[_color] for _color, _max in _maxes.items()):
            _result += _index
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

