"""The file that contains the ceaser cipher. you shouldn't be here."""
from ciphernoob.__utils import ALPHABET


def ceaser(text: str, key: int, encrypt=True) -> str:
    """Implementation of the ceaser cipher. (Also known as the
    shift/substitution cipher). The parameter 'text' takes in either
    plaintext or ciphertext, 'key' is the key for the cipher, and
    the 'encrypt' parameter either decides whether the text is encrypted or decrypted.
    See wikipedia.org/wiki/Caesar_cipher for more information about this cipher.
    Made in the China, by SoggyWetWater."""
    new_text = ""
    if not encrypt:
        key *= -1
    for character in text:
        if character.lower() in ALPHABET:
            shift = ALPHABET.find(character) + key
            print(shift)
            shift -= 26 if shift > 25 else 0
            new_character = ALPHABET[shift]
            if character.isupper():
                new_character = new_character.upper()
        else:
            new_character = character
        new_text += new_character
    return new_text
