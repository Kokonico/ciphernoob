# not needed for projects involving ciphers package, just an example.

# I'm aware it's a mess. I'm not going to fix it.

import ciphers

ciphers.adfgvx("hello world", True)
while True:
  request = input("""What do you want to do?
  1: encrypt.
  2: decrypt.
  """)
  # checks if user requested encrypt or decrypt
  if request == "1": # if requested encrypt
    cipher_text = input("enter top secret info: ")
    offset_number = int(input("select offset key (must be number, preferably big.): "))
    print(ciphers.kocrypt(cipher_text, offset_number, True))
  else:
    if request == "2": # if requested decrypt
      offset_code = input("enter what you would like to decrypt: ")
      offset_key = int(input("enter the key to said encryption: "))
      print(ciphers.kocrypt(offset_code, offset_key, False))
    else:
      # tell the user what they are supposed to do
      # because they can't follow basic instructions.
      print('''usage:
      "1": encrypt.
      "2": decrypt. 
      ''')