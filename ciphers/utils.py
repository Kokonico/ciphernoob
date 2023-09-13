"""General purpose variables and functions used throughout the package internally.
not meant for outer-package uses."""

# General purpose variables
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
CHARACTERS = '''!@#$%^&*)(-=_+}{][|'" ~`><,.?/:;'''
NUMBERS = '0123456789'

# General purpose functions
def get_case(letter: str):
  """Takes in a letter and returns True if it's a capitol."""
  return letter in ALPHABET.lower()
  # mush two numbers together withou adding them.
def ncon(num1, num2):
  num1 = str(num1)
  num2 = str(num2)
  return int(num1 + num2)