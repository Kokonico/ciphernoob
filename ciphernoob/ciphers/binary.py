from ciphernoob import __utils


def binary(message: str, mode: bool):

  if mode:
    # encryption
    return ''.join(format(ord(i), '08b') for i in message)
  else:
    # decryption
    bytes = __utils.chunk_string(message, 8)
    return ''.join(chr(int(binary, 2)) for binary in bytes)