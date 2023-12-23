# Imports

# Vanilla Python Modules

from itertools import pairwise

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day10_test.txt"
TEST_ANSWER = 8
PUZZLE_DATA = "./data/day10.txt"

NORTH = ["|", "L", "J"]
SOUTH = ["|", "7", "F"]
EAST = ["-", "L", "F"]
WEST = ["-", "J", "7"]

# Private Functions

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
   
    _xMax = len(_text[0]) - 1

    # Find the start location
    _sLoc = None
    for _y, _line in enumerate(_text):
        for _x, _char in enumerate(_line):
            if _char == "S":
                _sLoc = (_x, _y)
                break
        else:
            continue
        break
    # Calculate the distances for each space from start
    _dist = 0
    _next = []
    _spaces = {_sLoc: 0}
    if _sLoc[0] > 0 and _text[_sLoc[1]][_sLoc[0]-1] in EAST:
        _loc = (_sLoc[0] - 1, _sLoc[1])
        if _loc not in _spaces:
            _next.append(_loc)
    if _sLoc[0] < _xMax and _text[_sLoc[1]][_sLoc[0]+1] in WEST:
        _loc = (_sLoc[0] + 1, _sLoc[1])
        if _loc not in _spaces:
            _next.append(_loc)

    if _sLoc[1] > 0 and _text[_sLoc[1]-1][_sLoc[0]] in SOUTH:
        _loc = (_sLoc[0], _sLoc[1]-1)
        if _loc not in _spaces:
            _next.append(_loc)
    if _sLoc[0] < (len(_text)-1) and _text[_sLoc[1]+1][_sLoc[0]] in NORTH:
        _loc = (_sLoc[0], _sLoc[1]+1)
        if _loc not in _spaces:
            _next.append(_loc)

    while _next:
        _newNext = []
        _dist += 1
        for _loc in _next:
            _char = _text[_loc[1]][_loc[0]]
            _spaces[_loc] = _dist
            if _char in NORTH:
                _nLoc = (_loc[0], _loc[1] - 1)
                if _nLoc not in _spaces:
                    _newNext.append(_nLoc)
            if _char in SOUTH:
                _nLoc = (_loc[0], _loc[1] + 1)
                if _nLoc not in _spaces:
                    _newNext.append(_nLoc)
            if _char in EAST:
                _nLoc = (_loc[0] + 1, _loc[1])
                if _nLoc not in _spaces:
                    _newNext.append(_nLoc)
            if _char in WEST:
                _nLoc = (_loc[0] - 1, _loc[1])
                if _nLoc not in _spaces:
                    _newNext.append(_nLoc)
        _next = _newNext
    _result = sorted(_spaces.values())[-1]
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

