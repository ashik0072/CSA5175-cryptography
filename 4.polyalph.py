ct=str(input("ENTER THE CIPHER TEXT : "))
k=str(input("ENTER THE KEY : "))
letter="abcdefghijklmnopqrstuvwxyz"
dec=""
for x in ct:
        if x in letter:
            ctnum=letter.find(x)
            for y in k:
                if y in letter:
                    knum=letter.find(y)
                    total=(ctnum+knum)%26
                dec+=letter[total]
print("PLAIN TEXT : "+dec)

