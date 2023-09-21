"""autokey cipher."""

from ciphers import utils


def autokey(cmd: str, keyword: str, mode: bool, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    key = keyword.upper() + "".join(cmd.split()).upper()
    cmdup = cmd.upper()
    # create grid
    grid = {}
    current_alpha = alphabet
    for i in range(len(alphabet)):
        current_alpha = utils.str_rotate(alphabet, i)
        grid[i] = current_alpha
    if mode:
        # convert plaintext & key to numbers for coord locating
        numcmd = []
        numkey = []
        for i in key:
            numkey.append(int(utils.get_index(alphabet, i)))
        # crop it to match length of cmd

        numkey = numkey[: len(cmd)]
        for i in cmdup:
            numcmd.append(int(utils.get_index(alphabet, i)))

        # create final ciphertext using coords

        result = ""
        tres = ""
        for index, i in enumerate(numcmd):
            tres += grid[i]
            result += tres[index]

        # return result
        return result
    else:
        # TODO: decryption
        return "decrypt"