import os
from Crypto.Cipher import AES
import base64
import hashlib

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    iv = encrypted_data[:16]
    encoded_encrypted_data = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encoded_encrypted_data)
    return decrypted_data.rstrip(b'\x00')

def get_key(password):
    return hashlib.md5(password.encode()).digest()

def decrypt_all_files_in_folder(folder_path, password):
    key = get_key(password)
    for filename in os.listdir(folder_path):
        decrypted_data = decrypt_file(os.path.join(folder_path, filename), key)
        with open(os.path.join(folder_path, filename.replace('.uajs', '')), 'wb') as file:
            file.write(decrypted_data)

folder_path = input("Path : ")
password = '123123'

decrypt_all_files_in_folder(folder_path, password)
