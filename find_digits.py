l=[]
for i in range(2):
    n=int(input("Enter the number:"))
    l.append(n)
for i in l:
    if(i<=9):
        print(i,"is single digit")
    elif(i<=99):
        print(i,"is two digit numbers")
    elif(i<=999):
        print(i,"is 3 digit numbers")
    elif(i<=9999):
        print(i,"is 4 digit numbers")
    else:
        print(i)
