# Imports

# Vanilla Python Modules

import re

# Local Modules

import constants as c
import utils


# Constants

TEST_DATA = "./data/day01_p2_test.txt"
TEST_ANSWER = 281
PUZZLE_DATA = "./data/day01.txt"
REG_EXP = r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"

    
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
        _numbers = re.findall(REG_EXP, _line)
        _result += int("{}{}".format(
            c.NUMBER_SUBS.get(_numbers[0], _numbers[0]),
            c.NUMBER_SUBS.get(_numbers[-1], _numbers[-1])          
        ))
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

