"""the file that contains the adfgvx cipher. not intended for human eyes."""
from ciphers.utils import (
    ALPHABET,
    CHARACTERS,
    NUMBERS,
    chunk_string,
    d_mush,
    r_check,
    row_column_converter,
)


def adfgvx_gen(key):
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

    if mode:
        # Encryption
        grid = adfgvx_gen(alphamap) if not isinstance(alphamap, dict) else alphamap
        for i in cmd:
            if i in grid:
                intermediate += "".join(grid[i])

        rows = chunk_string(intermediate, len(col_key))
        columns = row_column_converter(rows, False)
        result = {i: columns[int(i)] for i in col_order}

        return " ".join(result.values())
    else:
        # Decryption goes here