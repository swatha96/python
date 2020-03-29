number=int(input("enter the number:"))
sums=0
while(number>0):
    r=number%10
    number=number//10
    sums=sums+r
print(sums)
