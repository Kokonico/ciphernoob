# TODO: make the actual product.

from ciphers.general_purpose import ncon


class Object(object):
  pass

def adfgvx(input, mode: bool):
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""
  # generate grid for encyphering.
  gridx = 0
  gridy = 1
  grid = {}
  # generate grid values.
  for i in input:
    if i not in grid:
      gridx += 1
      if gridx == 6:
        gridx = 0
        gridy += 1
      grid[i] = ncon(gridx, gridy)
  print(grid)