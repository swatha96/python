"""
number=[23,98,56,26,96,63]
number.sort()
maxi=len(number)
minus=maxi-1
for i in range(maxi):
    if(i==minus):
        print("the largest number is :",number[i])

"""

    
number=[]
n=int(input("how many numbers you wants to add:"))
for i in range(n):
    num=int(input("enter the number:"))
    number.append(num)
number.sort()
maxi=len(number)
minus=maxi-1
for i in range(maxi):
    if(i==minus):
        print("the largest number is :",number[i])
