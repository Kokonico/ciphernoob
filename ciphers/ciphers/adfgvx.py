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

# this will be useful later i swear
CMAP = "ADFGVX"


def adfgvx_gen(key):
    """generate a gridmap for the adfgvx cipher."""
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
    return grid


def adfgvx(cmd: str, col_key: str, alphamap, mode: bool):
    """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""
    if r_check(cmd):
        # generate grid variables.
        grid = {}
        col_map = {}
        intermediate = ""
        map2 = {}
        col_order = int()
        # map colume key values to letters
        for index, j in enumerate(col_key):
            col_map[j] = index
        # now sort the letters alphabetically
        map2 = {k: col_map[k] for k in sorted(col_map.keys())}
        # now grab the order of numbers.
        col_map = map2
        col_order = list(d_mush(col_map))  # dont know why this is throwing a error
        # it dosn't crash the project, so i'll leave it
        # generate grid values.
        if mode:
            if not isinstance(alphamap, dict):
                grid = adfgvx_gen(alphamap)

            # convert the numbers into ADFGVX
            for i in grid:
                grid[i] = [CMAP[grid[i][0]], CMAP[grid[i][1]]]

            for i in cmd:
                if i in grid:
                    intermediate += "".join(grid[i])
            counter = 1
            rows = {}
            for i in chunk_string(intermediate, len(col_key)):
                rows[counter] = i
                counter += 1  # get rows left to right
            # convert rows from left to right to columns (up to down)
            columns = row_column_converter(rows)
            result = {}
            counter = 0
            for i in col_order:
                result[i] = columns[int(i)]  #
                counter += 1
            return " ".join(result.values())


# add else here
