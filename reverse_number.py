number=int(input("enter the number:"))
reverse=0
while(number>0):
    r=number%10
    number=number//10
    reverse=(reverse*10)+r
print(reverse)
