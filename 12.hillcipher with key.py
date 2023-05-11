import numpy as np

key = np.array([[9, 4], [5, 7]])

def string_to_matrix(s):
    return np.array([ord(c) - 97 for c in s])

def matrix_to_string(matrix):
    return ''.join([chr(int(x) + 97) for x in matrix])

def hill_cipher_encrypt(message):
    message_matrix = string_to_matrix(message)
    message_matrix = np.reshape(message_matrix, (-1, 2)).T
    len = message_matrix.shape[1]
    encrypted_matrix = np.mod(np.dot(key, message_matrix), 26)
    encrypted_message = matrix_to_string(encrypted_matrix.T.flatten())
    return encrypted_message

message = "meet me at the usual place at ten rather than eight oclock"
encrypted_message = hill_cipher_encrypt(message)
print(encrypted_message)
