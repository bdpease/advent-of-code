# Imports

# Vanilla Python Modules

import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day08_p1_test1.txt"
TEST_ANSWER = 2
TEST_DATA2 = "./data/day08_p1_test2.txt"
TEST_ANSWER2 = 6
PUZZLE_DATA = "./data/day08.txt"

NODE_REGEX = r"([A-Z]+)\s\=\s\(([A-Z]+),\s([A-Z]+)"


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

    _currentNode = "AAA"
    _currentInstruction = 0
    while _currentNode != "ZZZ":
        _instruction = _instructions[_currentInstruction]
        _currentNode = _nodes[_currentNode][int(_instruction)]
        _currentInstruction += 1
        _result += 1
        if _currentInstruction >= len(_instructions):
            _currentInstruction = 0
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

