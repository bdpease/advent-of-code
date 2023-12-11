# Imports

# Vanilla Python Modules

from collections import Counter

# Local Modules

import utils


# Constants

TEST_DATA = "./data/day07_test.txt"
TEST_ANSWER = 5905
PUZZLE_DATA = "./data/day07.txt"
HAND_TYPES = {
    '5': 0,
    '14': 1,
    "23": 2,
    "113": 3,
    "122": 4,
    "1112": 5,
    "11111": 6
}
CHAR_MAP = str.maketrans({
    "A": "a",
    "K": "b",
    "Q": "c",
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m",
    "J": "n",
})


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
    
    _handsByType = {}
    for _line in _text:
        _hand, _bet = _line.split(" ")
        _jCount = _hand.count("J")
        if _jCount == 5:
            _handType = HAND_TYPES["5"]
        else:
            _handTmp = _hand.replace("J", "").translate(CHAR_MAP)
            _handTypeKey = "".join(sorted([str(_handTmp.count(c)) for c in set(_handTmp)]))            
            _handTypeKey = _handTypeKey[:-1] + str(int(_handTypeKey[-1]) + _jCount)
            _hand = _hand.translate(CHAR_MAP)
        _handType = HAND_TYPES[_handTypeKey]
        _handsByType.setdefault(_handType, []).append((_hand, _bet))
    _finalRanking = []
    for i in range(len(HAND_TYPES)):
        _hands = _handsByType.get(i)
        if not _hands:
            continue
        _hands = sorted(_hands, key=lambda x: x[0])
        _finalRanking += _hands
    for i, _hand in enumerate(reversed(_finalRanking)):
        _result += int(_hand[1]) * (i + 1)
    return _result


# Main

if __name__ == "__main__":
    _calculate(PUZZLE_DATA)

