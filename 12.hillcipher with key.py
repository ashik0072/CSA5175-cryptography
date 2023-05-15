matrix=[[2,3],[3,4]]
plain=str(input("ENTER THE PLAIN TEXT : "))
letter="abcdefghijklmnopqrstuvwxyz"
cipher=""
array=[]
after_mul=[]
for i in plain:
    if i in letter:
        pos=letter.find(i)
        array.append(pos)
for i in range(0,len(array),2):
    a,b=array[i],array[i+1]
    c,d=((a*matrix[0][0])+(b*matrix[1][0])),((a*matrix[0][1])+(b*matrix[1][1]))
    e,f=(c%26),(d%26)
    after_mul.append(e)
    after_mul.append(f)
for i in after_mul:
    cipher+=letter[i]
print(cipher)
