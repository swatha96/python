a=input("enter the word:")
b=input("enter the word:")
common_charactor=""
for i in a:
    for j in b:
        if(i==j):
            common_charactor=common_charactor+i
common=list(common_charactor)
print("common charactors are ",common) 
