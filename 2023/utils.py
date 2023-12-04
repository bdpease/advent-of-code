# Imports

# Local Modules

import constants as c


# Decorators

def test_puzzle(test_data, test_answer):
    """Decorator to test the puzzle code and print out the generated answer, if test is passed."""
    def wrap(func):
        def wrapped(*args):
            _test_result = func(test_data)
            if _test_result == test_answer:
                print("Test Passed! Correct answer of `{}` generated!".format(str(test_answer)))
                _puzzle_result = func(*args)
                print("Generated puzzle answer: `{}`".format(str(_puzzle_result)))
                return _puzzle_result
            else:
                print(
                    "Test Failed! Incorrect answer of `{}` generated! Answer should be `{}`.".format(
                        str(_test_result),
                        str(test_answer)
                    )
                )
        return wrapped
    return wrap


# Public Functions

def read_doc(input_path):
    """Read the document at the given path.
    
    Args:
        input_path (str): Path of the document to read.

    Returns:
        list[str]
    """
    with open(input_path, "r") as _doc:
        _lines = [_line.replace(c.NEWLINE_CHAR, "") for _line in _doc.readlines()]
    return _lines

