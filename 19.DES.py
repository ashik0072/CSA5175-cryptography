from Crypto.Cipher import DES3
import os

key = os.urandom(24)
iv = os.urandom(8)

cipher = DES3.new(key, DES3.MODE_CBC, iv)

message = b"Hello, world!"

pad_len = 8 - (len(message) % 8)
message += bytes([pad_len]) * pad_len

ciphertext = iv + cipher.encrypt(message)

print(ciphertext)
