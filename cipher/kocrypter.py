import cipher.shared


def kocrypter_encrypt(cmdinput, cmdkey):
    """Encrypts plain text by shifting and converting into numbers."""
    offset_number = int(cmdkey)
    pos = offset_number
    output = ""
    outlist = []

    # Calculate the true shift value
    numre = 0
    trueshift = 0
    alphabet_length = len(cipher.shared.ALPHABET)

    while numre != offset_number:
        numre += 1
        trueshift += 1
        if trueshift >= alphabet_length:
            trueshift = 0

    for x in cmdinput:
        if x in cipher.shared.ALPHABET:
            n = (cipher.shared.ALPHABET.index(x) + offset_number + trueshift) % alphabet_length
            n = str(n)
            outlist.append(n)

    pos %= len(outlist)
    output = '/'.join(map(str, outlist[-pos:] + outlist[:-pos]))
    return output

  #Kocrypter decrypt

def kocrypter_decrypt(cmdinput, cmdkey):
    """Decrypt the kocrypter cipher, assuming you know the key."""
    offset_code = cmdinput
    offset_key = int(cmdkey)
    reverse_offset = offset_key * -1
    inlist = offset_code.split("/")
    offpos = reverse_offset
    offpos %= len(inlist)
    inlist = inlist[-offpos:] + inlist[:-offpos]
    inlist2 = []
    result = []

    # Calculate the true shift value for decryption
    numre = 0
    trueshift = 0
    alphabet_length = len(cipher.shared.ALPHABET)

    while numre != offset_key:
        numre += 1
        trueshift += 1
        if trueshift >= alphabet_length:
            trueshift = 0

    # Remove offset using the key
    for a in inlist:
        n = (int(a) - offset_key - trueshift) % alphabet_length
        n = str(n)
        inlist2.append(n)

    # Convert back to regular characters
    for y in inlist2:
        if y.isdigit():
            result.append(cipher.shared.ALPHABET[int(y)])

    return ''.join(result)