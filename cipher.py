"""A module full of functions for encoding and decoding messages from classical ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers. https://inventwithpython.com/cracking/"""

# git enabled. press "git" in tools -Koko

# for kocrypter
ALPHA1 = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'''
AlPHA2 = ''':;/|!@#$%^&*()_+-=}{][?><,.'" '''
ALPHABET = ALPHA1 + AlPHA2

# ADFGVX
  
def adfgvx():
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""

# ROT13

def rot(text, rotation_number):
  """ROT cipher, based off of ROT13, uses substitution to encrypt text."""
  numre = 0
  trueshift = 0
  while numre != rotation_number:
    numre += 1
    trueshift += 1
    if trueshift > len(ALPHABET):
      trueshift = 0
  output = ""
  for x in text:
    n = 2
    while x != ALPHABET[n - 2]:
      n += 1
    n = n + trueshift
    if n > len(ALPHABET):
      n = len(ALPHABET) - n
    output = output + ALPHABET[n]
    return output
# kocrypter

def kocrypter_encrypt(cmdinput, cmdkey):
    """Encrypts plain text by shifting and converting into numbers."""
    offset_number = int(cmdkey)
    pos = offset_number
    output = ""
    outlist = []

    # Calculate the true shift value
    numre = 0
    trueshift = 0
    alphabet_length = len(ALPHABET)

    while numre != offset_number:
        numre += 1
        trueshift += 1
        if trueshift >= alphabet_length:
            trueshift = 0

    for x in cmdinput:
        if x in ALPHABET:
            n = (ALPHABET.index(x) + offset_number + trueshift) % alphabet_length
            n = str(n)
            outlist.append(n)

    pos %= len(outlist)
    output = '/'.join(map(str, outlist[-pos:] + outlist[:-pos]))
    return output

# DECRYPT AREA #

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
    alphabet_length = len(ALPHABET)

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
            result.append(ALPHABET[int(y)])

    return ''.join(result)