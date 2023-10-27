"""autokey cipher."""

from ciphernoob import __utils as utils


def autokey(plaintext, keyword, mode=True, alphabet=utils.ALPHABET_UPPER):
    """the autokey cipher."""
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    key = keyword + plaintext
    ciphertext = ""
    
    for i in range(len(plaintext)):
        if plaintext[i] not in alphabet:
            ciphertext += plaintext[i]
        else:
            plaintext_index = utils.get_index(alphabet, plaintext[i])
            key_index = utils.get_index(alphabet, key[i])
            
            if mode:  # Encryption mode
                cipher_index = (plaintext_index + key_index) % len(alphabet)
            else:  # Decryption mode
                cipher_index = (plaintext_index - key_index) % len(alphabet)
            
            ciphertext += alphabet[cipher_index]
            key += alphabet[cipher_index]
    
    return ciphertext
