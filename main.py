"""A module full of functions for encoding and decoding messages from classical ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers. https://inventwithpython.com/cracking/"""

#git enabled. press "git" in tools -Koko

#for offset cypher
ALPHA1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
AlPHA2 = ':;/|!@#$%^&*()_+-=}{][?><,." '
ALPHABET = ALPHA1 + AlPHA2

  
def adfgvx():
  """The ADFGVX cipher. Informations at en.wikipedia.org/wiki/ADFGVX_cipher."""

# offset cypher

def offset_cipher():
  """ciphers plain text via offsetting and converting into numbers."""
  cipher_text = input("enter top secret info: ")
  offset_number = int(input("select offset key (must be number, preferably big.): "))
  pos = offset_number
  output = ""
  outlist = []
  for x in cipher_text:
    n = 2
    while x != ALPHABET[n - 2]:
      n += 1
    n = str(n + offset_number)
    outlist.append(n)
    n = int(n)
  pos %= len(outlist)
  output = '/'.join(map(str, outlist[-pos:] + outlist[:-pos]))
  print(output)

# DECRYPT AREA #

# offset dycrypt

# def offset_cipher_decrypt():


# MAIN

offset_cipher()