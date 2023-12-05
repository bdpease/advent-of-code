# Imports

# Vanilla Python Modules

import re

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day03_test.txt"
TEST_ANSWER = 467835
PUZZLE_DATA = "./data/day03.txt"

NUMBER_REG_EXP = r"([0-9]+)"
SYMBOL_REG_EXP = r"(\*)"


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
    _symbols = {}
    for _y, _line in enumerate(_text):
        for _match in re.finditer(NUMBER_REG_EXP, _line):
            for _sy, _symLine in enumerate(_text[max(_y-1, 0):min(_y+2, len(_text))]):
                for _symMatch in re.finditer(SYMBOL_REG_EXP, _symLine[max(_match.start()-1, 0):min(_match.end()+1, len(_line))]):
                    _symbols.setdefault((max(_match.start()-1,0)+_symMatch.start(),max(_y-1, 0)+_sy), []).append(int(_match.groups()[0]))
    for _numbers in _symbols.values():
        if len(_numbers) == 2:
            _result += _numbers[0]*_numbers[1]
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

