# this file makes sure you didn't break anything.

# if you change a cipher, make sure to change the test for said cipher accordingly.

# tests are meant to be checks to see if what you expect to happen, happens.

# USAGE:

# 1: make sure your test names start with "test"
# 2: run the following command in SHELL (NOT console) to test everything.

## python -m unittest discover -v ##

# general
import unittest

import cipher

t = cipher.ALPHABET
# kocrypter
class kocrypter(unittest.TestCase):

  def test_kocrypter_encrypt_to_decrypt(self):
    self.assertEqual(cipher.kocrypter_decrypt(cipher.kocrypter_encrypt(t, 287), 287), t)

# ROT

#class rot(unittest.TestCase):
#  def test_rot_encrypt_to_decrypt(self):
#    self.assertEqual(cipher.derot(cipher.rot(t, 13)), t)
  