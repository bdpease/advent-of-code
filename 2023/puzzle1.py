# Imports

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day01_p1_test.txt"
TEST_ANSWER = 142
PUZZLE_DATA = "./data/day01.txt"


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
        _numbers = "".join(filter(str.isdigit, _line))
        _result += int("".join([_numbers[0], _numbers[-1]]))
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

