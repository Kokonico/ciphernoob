"""A package full of functions 
for encoding and decoding messages from a variety of ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers."""
# note: to import new ciphers, use the others below.
from .ciphers.adfgvx import adfgvx, adfgvx_gen
from .ciphers.autokey import autokey
from .ciphers.binary import binary
from .ciphers.ceaser import ceaser
from .ciphers.kocrypter import kocrypt
from .ciphers.morse import morse
from .ciphers.piglat import piglat
