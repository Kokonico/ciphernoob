# tests to make sure you didn't break anything.

# to run tests type "python -m unittest tests" into shell.
import unittest

import ciphers
from ciphers import general_purpose

t = general_purpose.ALPHABET

# Kocrypter tests

class Kocrypter(unittest.TestCase):
  #check if decrypt is same as original input
  def test_encrypt_decrypt_clairity_kocrypter(self):
    self.assertEqual(ciphers.kocrypt(ciphers.kocrypt(t, 8423, True), 8423, False), t)

# Ceaser tests
class ceaser(unittest.TestCase):
  def test_encrypt_decrypt_clairity_ceaser(self):
    self.assertEqual(ciphers.ceaser(ciphers.ceaser(t, 15, True), 15, False), t)