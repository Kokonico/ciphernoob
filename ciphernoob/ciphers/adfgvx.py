"""Contains functions of the adfgvx cipher."""

from ciphernoob.__utils import (
    ALPHABET,
    CHARACTERS,
    NUMBERS,
    chunk_string,
    find_key,
    row_column_converter,
)


def adfgvx_gen(key):
    """Generates an alphamap for the adfgvx cipher."""
    cmap = "ADFGVX"
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
        new_grid[i] = [cmap[grid[i][0]], cmap[grid[i][1]]]
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

    # If alphamap is not an alphabet mapping, create one.
    grid = adfgvx_gen(alphamap) if not isinstance(alphamap, dict) else alphamap

    if mode:
        # Encryption
        for i in cmd:
            if i in grid:
                intermediate += "".join(grid[i])

        rows = chunk_string(intermediate, len(col_key))
        columns = row_column_converter(rows, False)
        result = {i: columns[int(i)] for i in col_order}
        return " ".join(result.values())
    else:
        # Convert input into columns.
        columns = cmd.split()
        # Map the columns to the letters in the key
        # and unshuffle those columns based on the col_key
        key_map = {}
        for index, i in enumerate(columns):
            key_map[col_order[index]] = i
        key_map = dict(sorted(key_map.items()))  # Unshuffle
        # Convert them back to rows.
        intermediate = "".join(row_column_converter(key_map, True).values())
        chars = chunk_string(intermediate, 2)
        coordlist = []
        for i in chars:
            coordlist.append(chunk_string(i, 1))
        # Find the characters using the alphabet map
        # And concatenate them into result.
        result = ""
        for i in coordlist:
            result += find_key(grid, i)
        return result
