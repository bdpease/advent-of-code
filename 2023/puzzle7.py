# Imports

# Vanilla Python Modules

import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day04_test.txt"
TEST_ANSWER = 13
PUZZLE_DATA = "./data/day04.txt"

NUMBERS_REG_EXP = r"(?:^Card\s+[0-9]+:\s+)([0-9\s]+)(?:\s\|\s)([0-9\s]+)"


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
        for _match in re.finditer(NUMBERS_REG_EXP, _line):
            _numbers = len(
                set(_match.groups()[1].replace("  ", " ").split(" ")) &
                set(_match.groups()[0].replace("  "," ").split(" "))
            )
            if _numbers > 0:
                _result += utils.double(1, _numbers-1)
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

