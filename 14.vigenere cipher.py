plaintext = 'sendmoremoney'
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
numbers = [ord(c) - ord('a') for c in plaintext]
ciphertext = ''
for i, num in enumerate(numbers):
    key_num = key[i % len(key)]
    encrypted_num = (num + key_num) % 26
    ciphertext += chr(encrypted_num + ord('a'))

print('Plaintext:', plaintext)
print('Key:', key)
print('Ciphertext:', ciphertext)
