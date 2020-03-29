lst=[]
num=int(input("enter the number:"))
if(num==0):
    print("process stoped thank  u")
while(num!=0):
    lst.append(num)
    num=int(input("enter the number:"))
    if(num==0):
        lst.sort()
        lst1=len(lst)
        l=int(lst1-1)
        print(lst[0],"is the minimum value\n",lst[l],"is the maximum value")

