pt=str(input("ENTER THE PLAIN TEXT : "))
n=int(input("ENTER THE SHIFT NUMBER : "))
enc=""
for i in range(len(pt)):
    ch=pt[i]
    if ch==" ":
        enc+=" "
    elif(ch.isupper()):
        enc+=chr((ord(ch)+n-65)%26+65)
    else:
        enc+=chr((ord(ch)+n-97)%26+97)
print("CIPHER TEXT : "+enc)
dec=""
ct=str(input("ENTER THE CIPHER TEXT : "))
N=int(input("ENTER THE SHIFT NUMBER : "))
letter="abcdefghijklmnopqrstuvwxyz"
for x in ct:
    if x in letter:
        pos=letter.find(x)
        new_pos=(pos-N)%26
        new_char=letter[new_pos]
        dec+=new_char
    else:
        dec+=x
print("PLAIN TEXT : "+dec)
