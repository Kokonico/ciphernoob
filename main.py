import cipher

cipher_text = input("enter top secret info: ")
offset_number = int(input("select offset key (must be number, preferably big.): "))
print(cipher.kocrypter_encrypt(cipher_text, offset_number))
offset_code = input("enter what you would like to decrypt: ")
offset_key = int(input("enter the key to said encryption: "))
print(cipher.kocrypter_decrypt(offset_code, offset_key))