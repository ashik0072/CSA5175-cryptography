from Crypto.Cipher import AES
import binascii

def pad(data, block_size):
    padding = block_size - len(data) % block_size
    return data + b"\x80" + (padding - 1) * b"\x00"
    
def unpad(data):
    # Remove the padding from the data
    return data.rstrip(b"\x00").rstrip(b"\x80")

def encrypt_ecb(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    return plaintext

def encrypt_cbc(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_cbc(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    return plaintext

def encrypt_cfb(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_cfb(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    return plaintext
    
key = b"This is a 16-byte key"
iv = b"This is a 16-byte iv"
plaintext = b"Hello world! This is a test."
print("Plaintext: ", plaintext)

ciphertext = encrypt_ecb(key, plaintext)
print("ECB ciphertext: ", binascii.hexlify(ciphertext))
decrypted_plaintext = decrypt_ecb(key, ciphertext)
print("ECB decrypted plaintext: ", decrypted_plaintext)

ciphertext = encrypt_cbc(key, iv, plaintext)
print("CBC ciphertext: ", binascii.hexlify(ciphertext))
decrypted_plaintext = decrypt_cbc(key, iv, ciphertext)
print("CBC decrypted plaintext: ", decrypted_plaintext)

ciphertext = encrypt_cfb(key, iv, plaintext)
print("CFB ciphertext: ", binascii.hexlify(ciphertext))
decrypted_plaintext = decrypt_cfb(key, iv, ciphertext)
print("CFB decrypted plaintext: ", decrypted_plaintext)
