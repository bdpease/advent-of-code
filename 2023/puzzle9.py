# Imports

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day05_test.txt"
TEST_ANSWER = 35
PUZZLE_DATA = "./data/day05.txt"


# Private Functions

def _constructConversion(destStart, sourceStart, length):
    """Construct the conversion info for the given dest start, source start, and range length.
    
    Args:
        destStart (int): Starting index of the destination range.
        sourceStart (int): Starting index of the source range.
        length (int): Length of the range.
    
    Returns:
        tuple(int, int, int)
    """
    return (int(sourceStart), int(sourceStart) + int(length) - 1, int(destStart) - int(sourceStart))


@utils.test_puzzle(TEST_DATA, TEST_ANSWER)
def _calculate(input_path):
    """Calculate the result from the given input data.

    Args:
        input_path (str): Path to a file containing the input data to process.

    Returns:
        str | int
    """
    _result = -1
    _text = utils.read_doc(input_path=input_path)
    _seeds = None
    _conversionSets = []
    _currentSet = []
    for _line in _text:
        if _line.startswith("seeds: "):
            _seeds = _line.split(": ")[1].split(" ")
        elif _line.endswith(" map:"):
            if len(_currentSet) > 0:
                _conversionSets.append(_currentSet)
                _currentSet = []
        elif _line == "":
            continue
        else:
            _currentSet.append(_constructConversion(*_line.split(" ")))
    _conversionSets.append(_currentSet)
    for _seed in _seeds:
        _currentVal = int(_seed)
        for _conversionSet in _conversionSets:
            for _conversion in _conversionSet:
                if _conversion[0] <= _currentVal <= _conversion[1]:
                    _currentVal += _conversion[2]
                    break
        if _result == -1 or _currentVal < _result:
            _result = _currentVal
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

