# this file makes sure you didn't break anything.

# if you change a cipher, make sure to change the test for said cypher accordingly.

# general
import unittest

import cipher

t = "sample message"
# kocrypter
class kocrypter(unittest.TestCase):

  def encrypt_to_decrypt(self):
    self.assertEqual(cipher.kocrypter_decrypt(cipher.kocrypter_encrypt(t, 22), 22), t)