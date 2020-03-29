a=[]
n=int(input("Enter how many numbers which unwant to add in list:"))
print("enter the value one by one")
for i in range(n):
    b=int(input("enter the number:"))
    a.append(b)
print(a)
a.sort()
minus=int(len(a)-1)
times=0
for i in a:
    times=times+1
    if(times==minus):
        print("The second largest value in list is:",i)
