"""A module full of functions for encoding and decoding messages from classical ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers. https://inventwithpython.com/cracking/"""

# git enabled. press "git" in tools -Koko

# for kocrypter
ALPHA1 = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'''
AlPHA2 = ''':;/|!@#$%^&*()_+-=}{][?><,.'" '''
ALPHABET = ALPHA1 + AlPHA2

  
def adfgvx():
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""

# kocrypter

def kocrypter_encrypt(cmdinput, cmdkey):
  """ciphers plain text via offsetting and converting into numbers. Made by me, Koko."""
  cipher_text = cmdinput
  offset_number = int(cmdkey)
  pos = offset_number
  output = ""
  outlist = []
  #Get ROT
  numre = 0
  trueshift = 0
  while numre != offset_number:
    numre += 1
    trueshift += 1
    if trueshift > len(ALPHABET):
      trueshift = 0
  for x in cipher_text:
    n = 2
    while x != ALPHABET[n - 2]:
      n += 1
    n = str(n * offset_number - offset_number + trueshift)
    outlist.append(n)
    n = int(n)
  pos %= len(outlist)
  output = '/'.join(map(str, outlist[-pos:] + outlist[:-pos]))
  return output

# DECRYPT AREA #

  #Kocrypter decrypt

def kocrypter_decrypt(cmdinput, cmdkey):
  """decrypt the offset cipher, assuming you know the key."""
  offset_code = cmdinput
  offset_key = int(cmdkey)
  reverse_offset = offset_key * -1
  inlist = offset_code.split("/")
  offpos = reverse_offset
  offpos %= len(inlist)
  inlist = inlist[-offpos:] + inlist[:-offpos]
  inlist2 = []
  result = []
  numre = 0
  trueshift = 0
  while numre != offset_key:
    numre += 1
    trueshift += 1
    if trueshift > len(ALPHABET):
      trueshift = 0
  
  # remove offset via key
  for a in inlist:
    inlist2.append(int(a) / offset_key + offset_key - trueshift)
  # convert to regular characters
  for y in inlist2:
    result.append(ALPHABET[int(y) - 2])
  return ''.join(result)