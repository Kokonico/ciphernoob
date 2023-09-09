<<<<<<< HEAD:cipher/ciphers/ceaser.py
<<<<<<< HEAD:cipher/classical.py
=======
from cipher.general_purpose import ALPHABET
=======
from ciphers.general_purpose import ALPHABET
>>>>>>> 766e9d7 (cleaned up & removed unnecessary files.):ciphers/ciphers/ceaser.py

# does not pass encrypt to decrypt test.
# todo: fix
def ceaser(text: str, key: int, mode: bool, capitals: bool = False):
  """The ceaser (or substitution) cipher. The text parameter takes in plaintext or 
  ciphertext, the key takes in a key (does NOT validate it through), and mode takes in
  a boolean value (True = incrypt, False = decrypt)."""

  if not mode:
    key *= -1
  new_text = ''
  for character in text:
    turn = 0
    if character.lower() in ALPHABET.lower():
      if (ALPHABET.index(character.lower()) + key) > 25:
        turn = 25
      new_character = ALPHABET[(ALPHABET.index(character.lower()) + key) -
                               turn]
      if character != character.lower():
        new_text += new_character.upper()
      else:
        new_text += new_character
    else:
      new_text += character
  return new_text
>>>>>>> 4280175 (implemented new file storage, awaiting approval from soggywetwater.):cipher/ciphers/ceaser.py
