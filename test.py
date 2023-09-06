# this file makes sure you didn't break anything.

# if you change a cipher, make sure to change the test for said cipher accordingly.

# USAGE:

# 1: make sure your test names start with "test"
# 2: run the following command in shell to test everything.

## python -m unittest discover -v ##

# general
import unittest

import cipher

t = "sample message"
# kocrypter
class kocrypter(unittest.TestCase):

  def test_encrypt_to_decrypt(self):
    self.assertEqual(cipher.kocrypter_decrypt(cipher.kocrypter_encrypt(t, 22), 22), t)