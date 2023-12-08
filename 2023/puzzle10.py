# Imports

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day05_test.txt"
TEST_ANSWER = 46
PUZZLE_DATA = "./data/day05.txt"


# Private Functions

def _splitAndTranspose(rangeIn, mapping, shiftValue):
    """Split and transpose the source range based on the mapping range and shift value.
    
    Returns the untransposed differences and the transposed intersection of the ranges as start and end tuples.
    
    Args:
        rangeIn (tuple(int, int)): Start and end numbers of the range to split and transpose.
        mapping (tuple(int, int)): Start and end numbers of the mapping range.
        shiftValue (int): Amount to shift the intersection range by.
    
    Returns:
        list[tuple(int, int)], tuple(int, int)
    """    
    # Init some vars
    _differences = []
    _intersection = None
    # Check if there's an overlap between the source range and mapping range
    if not (rangeIn[0] < mapping[1] and rangeIn [1] > mapping [0]):
        # If no overlap, the whole source range is added to differences
        _differences.append(rangeIn)
    else:
        # If there is overlap, split the source range
        # Handle a left difference
        if rangeIn[0] < mapping[0]:
            _differences.append((rangeIn[0], mapping[0]-1))
        # Handle a right difference:
        if rangeIn[1] > mapping[1]:
            _differences.append((mapping[1]+1, rangeIn[1]))
        # Handle the intersection and transpose it
        _intersection = (
            max(rangeIn[0], mapping[0])+shiftValue, 
            min(rangeIn[1], mapping[1])+shiftValue
        )
    return _differences, _intersection


def _convertRange(rangeIn, mappings):
    """Convert a range based on the given mappings.
    
    Returns a list of the resulting range tuples.
    
    Args:
        rangeIn (tuple(int, int)): Start and end values of the range to convert.
        mappings (list[tuple(int, int, int)]): Mapping tuple of dest start, source start, and range.

    Returns:
        list[tuple(int, int)]
    """
    # Init some vars
    _ranges = [rangeIn]
    _converted = []
    # Iterate through each mapping
    for _mD, _mS, _mR in mappings:
        _mD = int(_mD)
        _mS = int(_mS)
        _mR = int(_mR)
        _newRanges = []
        # Iterate through all the current ranges and convert them based on the current mapping
        for _range in _ranges:
            _differences, _intersection = _splitAndTranspose(_range, (_mS, _mS + _mR - 1), _mD - _mS)
            # Store any converted data
            if _intersection:
                _converted.append(_intersection)
            # Store any unconverted data for later
            _newRanges += _differences
        # Replace the ranges with the unconverted ranges for the next mapping to handle
        _ranges = _newRanges
    # Any still unconverted ranges are considered converted
    _converted += _ranges
    return _converted


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
            _seedData = _line.split(": ")[1].split(" ")
            _seeds = list(zip(_seedData[::2], _seedData[1::2]))
        elif _line.endswith(" map:"):
            if len(_currentSet) > 0:
                _conversionSets.append(_currentSet)
                _currentSet = []
        elif _line == "":
            continue
        else:
            _currentSet.append(_line.split(" "))
    _conversionSets.append(_currentSet)
    
    for _seedStart, _seedRange in _seeds:
        _seedStart = int(_seedStart)
        _seedRange = int(_seedRange)
        _ranges = [(_seedStart, _seedStart + _seedRange - 1)]
        for _conversionSet in _conversionSets:
            _new_ranges = []
            for _range in _ranges:
                _new_ranges += _convertRange(_range, _conversionSet)
            _ranges = _new_ranges
        _ans = sorted([_r[0] for _r in _ranges])[0]
        if _result == -1 or _ans < _result:
            _result = _ans
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

