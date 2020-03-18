number=int(input("enter the number:"))
n1=0
n2=1
i=0
if(number<=0):
    print("enter the positive number")
elif number==1:
    print("fibonacci series upto:",number)
else:
    print("fibonacci series upto:",number)
    while(i<=number):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        i=i+1


