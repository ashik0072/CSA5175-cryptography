 import string
letter="ABCDEFGHIKLMNOPQRSTUVWXYZ"
modlett=""
pt_input=str(input("ENTER THE KEY : "))
pt=""
for i in pt_input:
    if i not in pt:
        pt+=i
for j in letter:
    if j not in pt:
        modlett+=j
matrix_ele=pt+modlett
matrix = [matrix_ele[i:i+5] for i in range(0, 25, 5)]
print("\nKEY MATRIX\n--------------")
for a in range(5):
    for b in range(5):
        print(matrix[a][b],end=" ")
    print()
def get_coordinates(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
plain=str(input("\nENTER THE PLAIN TEXT : "))
ciphertext = ""
for i in range(0, len(plain), 2):
    char1 = plain[i]
    char2 = plain[i+1] if i+1 < len(plain) else "X"
    row1, col1 = get_coordinates(matrix, char1)
    row2, col2 = get_coordinates(matrix, char2)
    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5
    elif col1 == col2:
        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5
    else:
        col1, col2 = col2, col1
    ciphertext += matrix[row1][col1] + matrix[row2][col2]
print("\nCIPHER TEXT : "+ciphertext)
    
