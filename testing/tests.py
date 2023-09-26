# tests to make sure you didn't break anything.

# to run tests type "python -m unittest testing.tests" into shell.
import unittest

import ciphernoob as ciphers
from ciphernoob import __utils as utils

t = utils.ALPHABET
n = utils.NUMBERS
d = {1: 4, 2: 7}
l = ["1", "2", "3", "4"]

# util tests

# TODO: implement tests for everything.
class util(unittest.TestCase):
  def test_n_mush(self):
    self.assertEqual(utils.n_mush(4,5), 45)
    
  def test_d_mush(self):
    self.assertEqual(utils.d_mush({1: "A", 2: "B"}), "AB")
    
  def test_getcase(self):
    self.assertEqual(utils.get_case("A"), True)
    self.assertEqual(utils.get_case("a"), False)
    
  def test_r_check(self):
    self.assertEqual(utils.r_check("apple"), False)
    self.assertEqual(utils.r_check("aple"), True)
    
  def test_find_key_check(self):
    self.assertEqual(utils.find_key(d, 4), 1)
    self.assertEqual(utils.find_key(d, 7), 2)

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
  
# Kocrypter tests

class Kocrypter(unittest.TestCase):
  def test_encrypt_decrypt_clairity_kocrypter(self):
    self.assertEqual(ciphers.kocrypt(ciphers.kocrypt(t, 8423, True), 8423, False), t)

# Ceaser tests
class ceaser(unittest.TestCase):
  def test_encrypt_decrypt_clairity_ceaser(self):
    self.assertEqual(ciphers.ceaser(ciphers.ceaser(t, 3, True), 3, False), t)
  def test_ceaser_parity(self):
    self.assertEqual(ciphers.ceaser("hello world", 3), "khoor zruog")

# ADFGVX tests
class adfgvx(unittest.TestCase):
  def test_encrypt_decrypt_clairity_adfgvx(self):
    key1 = "privacy"
    key2 = "helloworld"
        
    encrypted = ciphers.adfgvx(t + n, key1, key2, True)
    decrypted = ciphers.adfgvx(encrypted, key1, key2, False)
        
    self.assertEqual(decrypted, t + n)
  def test_adfgvx_parity(self):
    self.assertEqual(
      ciphers.adfgvx("helloworld", "privacy", "a", True),
      "DVA XFG AFD DXF DFX VGX DF"
    )

# autokey tests
class autokey(unittest.TestCase):
  def test_autokey_encrypt_decrypt_clarity(self):
    self.assertEqual(ciphers.autokey(ciphers.autokey(t, t), t, False), t.upper())
  def test_autokey_parity(self):
    self.assertEqual(ciphers.autokey("attackatdawn", "queenly", True), "QNXEPVYTWTWP")