import base64
from Crypto.Cipher import AES
import hashlib
import os
from os import path

def decrypt_file(file_path):
    encrypted_file = open(file_path, 'r').read()

    # Decode Base64
    decoded_data = base64.b64decode(encrypted_file)

    # Compute MD5 hash
    md5 = hashlib.md5()
    md5.update(decoded_data)
    key = md5.digest()

    # Decrypt AES
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(decoded_data).decode('utf-8')

    decrypted_file_path = file_path + "_decrypted"
    with open(decrypted_file_path, 'w') as f:
        f.write(decrypted_data)

    return decrypted_file_path

file_path = input("File path/dir to decrypt: ")

if path.exists(file_path):
    print("Decrypting...")
    decrypted_file_path = decrypt_file(file_path)
    print("Decrypt Success! Decrypted file saved at: " + decrypted_file_path)
else:
    print("File not found.")
