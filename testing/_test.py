# tests to make sure you didn't break anything.

# to run tests type "python -m unittest testing.tests" into shell

## !!! PLEASE READ TEST_ALIGNMENT_RULES !!! ##


import unittest

import ciphernoob as ciphers
from ciphernoob import __utils as utils

t = utils.ALPHABET
n = utils.NUMBERS
d = {1: 4, 2: 7}
l = ["1", "2", "3", "4"]

# util tests

class util(unittest.TestCase):

  
  # number mush
  
  def test_n_mush(self):
    self.assertEqual(utils.n_mush(4, 5), 45)


  # dictionary mush 
  
  def test_d_mush(self):
    self.assertEqual(utils.d_mush({1: "A", 2: "B"}), "AB")


  # get case
  
  def test_getcase(self):
    self.assertEqual(utils.get_case("A"), True)
    self.assertEqual(utils.get_case("a"), False)

  
  # repeating characters
  
  def test_r_check(self):
    self.assertEqual(utils.r_check("apple"), False)
    self.assertEqual(utils.r_check("aple"), True)

  
  # find key
  
  def test_find_key_check(self):
    self.assertEqual(utils.find_key(d, 4), 1)
    self.assertEqual(utils.find_key(d, 7), 2)


  # string chunk
  
  def test_chunk_string(self):
    
    self.assertEqual(utils.chunk_string("1234", 1), l)
    
    self.assertEqual(
      utils.chunk_string(t + n, 3), 
      ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz0', '123', '456', '789']
    )

    self.assertEqual(
        utils.chunk_string(t + n, 5),
        ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z0123', '45678', '9']
    )

  
  # string rotate

  def test_str_rotate(self):
    
    self.assertEqual(
      utils.str_rotate(t, 3), 
      "xyzabcdefghijklmnopqrstuvw"
    )
    
    self.assertEqual(
      utils.str_rotate(t, 26), 
      "abcdefghijklmnopqrstuvwxyz"
    )
    
    self.assertEqual(
      utils.str_rotate(t, 0), 
      "abcdefghijklmnopqrstuvwxyz"
    )




# Kocrypter tests

class Kocrypter(unittest.TestCase):

  
  # parity

  def test_encrypt_decrypt_clairity_kocrypter(self):
    for g in range(1000): # test with keys 1 - 1000
      self.assertEqual(
        ciphers.kocrypt(ciphers.kocrypt(t, g, True),
        g, False),
        t
      )




# Ceaser tests

class ceaser(unittest.TestCase):

  
  # encrypt/decrypt pairity

  def test_encrypt_decrypt_clairity_ceaser(self):
    for b in range(26): # test all reasonable keys
      self.assertEqual(
        ciphers.ceaser(ciphers.ceaser(t, b, True), b, False),
        t
      )


  # test if aligns with other ceaser ciphers.

  def test_ceaser_parity(self):
    self.assertEqual(
      ciphers.ceaser("hello world", 3),
      "khoor zruog"
    )




# ADFGVX tests

class adfgvx(unittest.TestCase):

  
  # parity

  def test_encrypt_decrypt_clairity_adfgvx(self):
    
    self.assertEqual(
      ciphers.adfgvx(
        ciphers.adfgvx(t + n, "privacy", "helloworld", True),
        "privacy", 
        "helloworld", 
        False
      ), 
      t + n
    )


  # alignment check

  def test_adfgvx_parity(self):
    
    self.assertEqual(
      ciphers.adfgvx("helloworld", "privacy", "a", True),
      "DVA XFG AFD DXF DFX VGX DF"
    )




# autokey tests

class autokey(unittest.TestCase):

  
  # parity
  
  def test_autokey_encrypt_decrypt_clarity(self):
    self.assertEqual(
      ciphers.autokey(ciphers.autokey(t, t), t, False),
      t.upper()
    )

  
  # match

  def test_autokey_parity(self):
    self.assertEqual(
      ciphers.autokey("attackatdawn", "queenly", True),
      "QNXEPVYTWTWP"
    )




# Binary

class binary(unittest.TestCase):

  
  # parity
  
  def test_binary_encrypt_decrypt_clarity(self):
    
    self.assertEqual(
      ciphers.binary(ciphers.binary(t, True), False), 
      t
    )

  # match

  def test_binary_parity(self):

    self.assertEqual(
      ciphers.binary("Man", True),
      "010011010110000101101110"
    )




# Morse

class morse(unittest.TestCase):

  
  # parity
  
  def test_morse_encrypt_decrypt_clarity(self):
    
    self.assertEqual(
      ciphers.morse(ciphers.morse(t + n, True), False),
      t + n
    )

  
  # match
  
  def test_morse_parity(self):
    
    self.assertEqual(
        ciphers.morse(t, True),
        ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    )



