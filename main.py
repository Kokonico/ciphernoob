# not needed for projects involving cipher package, just an example.

# import "kocrypter" cipher.
import cipher.kocrypter

while True:
  request = input("""What do you want to do?
  1: encrypt.
  2: decrypt.
  """)
  if request == "1":
    cipher_text = input("enter top secret info: ")
    offset_number = int(input("select offset key (must be number, preferably big.): "))
    print(cipher.kocrypter.kocrypter_encrypt(cipher_text, offset_number))
  else:
    if request == "2":
      offset_code = input("enter what you would like to decrypt: ")
      offset_key = int(input("enter the key to said encryption: "))
      print(cipher.kocrypter.kocrypter_decrypt(offset_code, offset_key))
    else:
      print('''usage:
      "1": encrypt.
      "2": decrypt. 
      ''')