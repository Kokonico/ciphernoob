from ciphers.utils import ALPHABET, CHARACTERS, NUMBERS


def adfgvx(input: str, mode: bool):
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""
  # generate grid variables.
  gridchars = input + ALPHABET + NUMBERS
  gridx = 0
  gridy = 0
  grid = {}
  # generate grid values.
  if mode:
    for i in gridchars:
      if i not in grid and i not in CHARACTERS:
        grid[i] = [gridx, gridy]
        gridx += 1
        if gridx == 6:
          gridx = 0
          gridy += 1 # behold, less garbage code.
    print(grid) #TODO: remove this.
# add else here