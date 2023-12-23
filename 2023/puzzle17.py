# Imports

# Vanilla Python Modules

from itertools import pairwise

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day09_test.txt"
TEST_ANSWER = 114
PUZZLE_DATA = "./data/day09.txt"

# Private Functions

def _predict(dataset):
    """Predict the next value from the given dataset."""
    if len(list(set(dataset))) == 1 and int(dataset[0]) == 0:
        return 0
    newDataset = [int(pair[1]) - int(pair[0]) for pair in pairwise(dataset)]
    difResult = _predict(newDataset)
    return int(dataset[-1]) + difResult

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
        _result += _predict(_line.split(" "))
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

