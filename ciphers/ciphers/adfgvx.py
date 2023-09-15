"""the file that contains the adfgvx cipher. not intended for human eyes."""
from ciphers.utils import (
    ALPHABET,
    CHARACTERS,
    NUMBERS,
    chunk_string,
    d_mush,
    find_key,
    r_check,
    row_column_converter,
)


def adfgvx_gen(key):
    """generate an alphamap for the adfgvx cipher."""
    CMAP = "ADFGVX"
    gridchars = key + ALPHABET + NUMBERS
    gridx = 0
    gridy = 0
    grid = {}
    for i in gridchars:
        if i not in grid and i not in CHARACTERS:
            grid[i] = [gridy, gridx]
            gridx += 1
            if gridx == 6:
                gridx = 0
                gridy += 1
    new_grid = {}
    for i in grid:
        new_grid[i] = [CMAP[grid[i][0]], CMAP[grid[i][1]]]
    grid = new_grid
    return grid


def adfgvx(cmd: str, col_key: str, alphamap, mode: bool):
    """the adfgvx cipher, developed by the germans for war."""
    if len(set(col_key)) != len(col_key):
        raise ValueError("col_key contains repeating characters")

    col_map = {}
    intermediate = ""
    map2 = {}
    col_order = int()

    for index, j in enumerate(col_key):
        col_map[j] = index

    map2 = {k: col_map[k] for k in sorted(col_map.keys())}
    col_map = map2
    col_order = list(col_map.values())

    # if alphamap is not an alphabet mapping, create one. 
    grid = adfgvx_gen(alphamap) if not isinstance(alphamap, dict) else alphamap
  
    if mode:
        # Encryption
        for i in cmd:
            if i in grid:
                intermediate += "".join(grid[i])

        rows = chunk_string(intermediate, len(col_key))
        columns = row_column_converter(rows, False)
        result = {i: columns[int(i)] for i in col_order}
        # this once was 60+ lines.
        # i have no clue how thats even possible.
        return " ".join(result.values())
    else:
      # decrypt
      # convert input into columns.
      columns = cmd.split()
      # we now unshuffle those columns based on the col_key
      # map the columns to the letters in the key
      key_map = {}
      for index, i in enumerate(columns):
        key_map[col_order[index]] = i
      # unshuffling
      key_map = dict(sorted(key_map.items()))
      # now with the unshuffled columns, we will convert them back to rows.
      intermediate = ''.join(row_column_converter(key_map, True).values())
      # we are now at the intermediate stage.
      # chunk the intermediate into lists of 2 characters
      chars = chunk_string(intermediate, 2)
      coordlist = []
      for i in chars:
        coordlist.append(chunk_string(i, 1))
      # find the characters using the alphabet map
      # and concatenate them into result.
      result = ""
      for i in coordlist:
        result += find_key(grid, i)
      return result