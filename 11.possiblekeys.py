import math
KEY_SIZE = 25
def num_possible_keys():
    total = 1
    for i in range(KEY_SIZE):
        total *= (KEY_SIZE - i)
    return total
keys = num_possible_keys()
print(f"The Playfair cipher has approximately {math.log2(keys):.2f} possible keys.")
