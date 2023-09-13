from ciphers.utils import ALPHABET, CHARACTERS, NUMBERS


def adfgvx(input: str, mode: bool):
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""
  # generate grid variables.
  chars = ALPHABET + NUMBERS
  gridx = 0
  gridy = 0
  grid = {}
  # generate reused code
  # generate grid values.
  if mode:
    for i in input:
      if i not in grid and i not in CHARACTERS:
        grid[i] = [gridx, gridy]
        gridx += 1
        if gridx == 6:
          gridx = 0
          gridy += 1
    for i in chars:
      if i not in grid and i not in CHARACTERS:
        gridx += 1
        if gridx == 6:
          gridx = 0
          gridy += 1
        grid[i] = [gridx, gridy] # behold, garbage code.
    print(grid) #TODO: remove this.
    for i in input:
      # I'll fix this tommorow.