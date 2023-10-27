from ciphernoob import __utils


def binary(message: str, mode: bool):
  """binary."""
  if mode:
    # encryption
    return ''.join(format(ord(i), '08b') for i in message)
  else:
    # decryption
    bytes = __utils.chunk_string(message, 8)

    for i in bytes:
      if len(i) > 8 or len(bytes) < 8:
        raise ValueError("malformed binary input")
    return ''.join(chr(int(binary, 2)) for binary in bytes)