"""A package full of functions 
for encoding and decoding messages from a variety of ciphers.
Ciphers found at en.wikipedia.org/wiki/Category:Classical_ciphers."""
# note: to import new ciphers, use the example below.
from .ciphers.adfgvx import adfgvx, adfgvx_gen
from .ciphers.ceaser import ceaser
from .ciphers.kocrypter import kocrypt
from .ciphers.piglat import piglat