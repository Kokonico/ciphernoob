"""General purpose variables and functions used throughout the package internally.
not meant for outer-package uses."""

# General purpose variables
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CHARACTERS = """!@#$%^&*)(-=_+}{][|'" ~`><,.?/:;"""
NUMBERS = "0123456789"


# General purpose functions
def get_case(letter: str):
    """Takes in a letter and returns True if it's a capital."""
    return letter in ALPHABET.lower()


def n_mush(num1, num2):
    """Concatenates two numbers together"""
    return num1 * (10 ** len(str(num2))) + num2


def d_mush(dictionary: dict):
    """Concatenates a dictionary's values into a string"""
    if isinstance(dictionary, dict):
        return "".join(str(val) for val in dictionary.values())
    else:
        raise TypeError("the provided value is not a dictionary.")

def r_check(x: str):
    """check for repeating characters"""
    return len(set(x)) == len(x)


def chunk_string(string, chunk_size):
    """chunks strings into small peices and keeps the remainder."""
    return [string[i : i + chunk_size] for i in range(0, len(string), chunk_size)]


def row_column_converter(input_data, is_dict):
    if is_dict:
        max_len = max(len(v) for v in input_data.values())
        result = {
            i: "".join(v[i % len(v)] if len(v) > i else "" for v in input_data.values())
            for i in range(max_len)
        }
    else:
        max_len = max(len(v) for v in input_data)
        result = {
            i: "".join(v[i % len(v)] if len(v) > i else "" for v in input_data)
            for i in range(max_len)
        }
    return result