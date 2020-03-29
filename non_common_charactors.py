a=input("enter the word:")
b=input("enter the word:")
noni=""
nonj=""
for i in a:
    c=0
    for j in b:
        if(i==j):
            c=0
        else:
            c=1
            nonj=non+j
    if(c==1):
        noni=non+i

print("non common charactors are:",noni,nonj)
