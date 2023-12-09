# Imports

# Vanilla Python Modules

import math
import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day06_test_p2.txt"
TEST_ANSWER = 71503
PUZZLE_DATA = "./data/day06_p2.txt"

NUMBER_REGEX = r"([0-9]+)"

# Private Functions

@utils.test_puzzle(TEST_DATA, TEST_ANSWER)
def _calculate(input_path):
    """Calculate the result from the given input data.

    Args:
        input_path (str): Path to a file containing the input data to process.

    Returns:
        str | int
    """
    _result = 1
    _text = utils.read_doc(input_path=input_path)
    
    _lines = [re.findall(NUMBER_REGEX, _line) for _line in _text]
    _raceRecords = list(zip(_lines[0], _lines[1]))
    for _record in _raceRecords:
        _raceTime = int(_record[0])
        _distRecord = int(_record[1])
        _tmp = math.sqrt(math.pow(_raceTime, 2) - (4 * _distRecord))
        _minCharge = 0.5 * (_raceTime - _tmp)
        _maxCharge = 0.5 * (_tmp + _raceTime)
        if _minCharge.is_integer():
            _minCharge = int(_minCharge) + 1
        else:
            _minCharge = math.ceil(_minCharge)
        if _maxCharge.is_integer():
            _maxCharge = int(_maxCharge) - 1
        else:
            _maxCharge = math.floor(_maxCharge)
        _result *= (_maxCharge - _minCharge + 1)

    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

