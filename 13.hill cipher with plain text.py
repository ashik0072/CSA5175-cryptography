import numpy as np
from sympy import Matrix

def convert_to_numbers(text):
    return [ord(ch) - ord('A') for ch in text]

def convert_to_string(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(' ', '')
    plaintext = convert_to_numbers(plaintext)
    n = len(key)
    if len(plaintext) % n != 0:
        plaintext += [0] * (n - len(plaintext) % n)
    plaintext = np.array(plaintext).reshape(-1, n)
    ciphertext = (np.dot(plaintext, key) % 26).flatten()
    return convert_to_string(ciphertext)

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(' ', '')
    ciphertext = convert_to_numbers(ciphertext)
    n = len(key)
    ciphertext = np.array(ciphertext).reshape(-1, n)
    key_inverse = Matrix(key).inv_mod(26)
    plaintext = (np.dot(ciphertext, key_inverse) % 26).flatten()
    return convert_to_string(plaintext)

known_pairs = [('HELLO', 'FJZSR'), ('WORLD', 'GYMZS')]

plaintexts = [convert_to_numbers(pair[0]) for pair in known_pairs]
ciphertexts = [convert_to_numbers(pair[1]) for pair in known_pairs]
n = len(known_pairs[0][0])
matrix_equations = []
for i in range(n):
    for j in range👎:
        equation = [plaintexts[k][i] * (j + 1) for k in range(len(known_pairs))]
        matrix_equations.append(equation)
matrix = Matrix(matrix_equations)
matrix_inverse = matrix.inv_mod(26)
key_matrix = matrix_inverse.applyfunc(lambda x: x % 26)

ciphertext = 'FJZSR'
decrypted_text = decrypt(ciphertext, key_matrix)

print("Determined Key Matrix:")
print(key_matrix)
print("\nDecrypted Text:")
print(decrypted_text)
