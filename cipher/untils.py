"""General purpose variables and functions used throughout the program."""

# General purpose variables
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
CHARACTERS = '1234567890!@#$%^&*()'

# General purpose functions
def get_case(letter: str):
  """Takes in a letter and returns True if it's a capital."""
  return letter in ALPHABET.lower()
