# Imports

# Vanilla Python Modules

import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day08_p2_test.txt"
TEST_ANSWER = 6
PUZZLE_DATA = "./data/day08.txt"

NODE_REGEX = r"([0-9]*[A-Z]+)\s\=\s\(([0-9]*[A-Z]+),\s([0-9]*[A-Z]+)"


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
    
    _instructions = _text[0].replace("L", "0").replace("R", "1")
    _nodes = {}
    for _line in _text[2:]:
        _node, _left, _right = re.match(NODE_REGEX, _line).groups()
        _nodes[_node] = (_left, _right)

    _startNodes = [_n for _n in _nodes.keys() if _n.endswith("A")]
    _currentInstruction = 0
    
    _currentNodes = [_startNodes[0]]
    while not all(_n.endswith("Z") for _n in _currentNodes):
        _instruction = _instructions[_currentInstruction]
        _newCurrentNodes = []
        for _currentNode in [_currentNode]:
            _newCurrentNodes.append(_nodes[_currentNode][int(_instruction)])
        _currentNodes = _newCurrentNodes
        _currentInstruction += 1
        _result += 1
        #if _result % 100000 == 0:
        #    print(_result)
        if _currentInstruction >= len(_instructions):
            _currentInstruction = 0
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

