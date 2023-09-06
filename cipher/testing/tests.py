# tests to make sure you didn't break anything.

# to run tests type "python -m unittest cipher.testing.tests" into shell.
import unittest

import cipher.kocrypter
import cipher.shared

t = cipher.shared.ALPHABET
class Kocrypter(unittest.TestCase):
  #check if decrypt is same as original input
  def test_encrypt_decrypt_clairity(self):
    self.assertEqual(
      cipher.kocrypter.kocrypter_decrypt(
        cipher.kocrypter.kocrypter_encrypt(t, 1584), 
        1584), 
      t)