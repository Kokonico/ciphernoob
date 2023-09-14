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
    # mush two numbers together withou adding them.


def n_mush(num1, num2):
    """Concatenates two numbers together"""
    num1 = str(num1)
    num2 = str(num2)
    return int(num1 + num2)


def d_mush(dictionary: dict):
    """Concatenates a dictionaries values into a string"""
    if isinstance(dictionary, dict):
        return "".join(str(val) for val in dictionary.values())
    else:
        TypeError("the provided value is not a dictionary.")


def chunkstring(string, length):
    """split strings into itty-bity peices"""
    counter = 0
    result = []
    internal_string = ""
    for i in string:
        counter += 1
        internal_string += i
        if counter == length:
            counter = 0
            result.append(internal_string)
            internal_string = ""
    return result


def r_check(x: str):
    """check for repeating characters"""
    return len(set(x)) == len(x)


def chunk_string(string, chunk_size):
    """chunks strings into small peices and keeps the remainder."""
    return [string[i : i + chunk_size] for i in range(0, len(string), chunk_size)]


def row_column_converter(input_dict):
    """merge the first letters of a dictionary with a length limit"""
    max_len = max(len(v) for v in input_dict.values())
    result = {}

    for i in range(max_len):
        row_values = [v[i % len(v)] if len(v) > i else "" for v in input_dict.values()]
        result[i] = "".join(row_values)

    return result
