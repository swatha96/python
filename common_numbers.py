lst1=[]
lst2=[]
n=int(input("how many numbers you wants to add:"))
for i in range(n):
    num1=int(input("enter the number in list1:"))
    lst1.append(num1)
    num2=int(input("enter the number in list2:"))
    lst2.append(num2)
print(lst1)
print(lst2)
common=[]
for i in lst1:
    for j in lst2:
        if(i==j):
            common.append(i)
print("common factors:",common)


"""

lst1=[23,89,56,86,96,8,6,9,99]
lst2=[8,6,9,66,88,77,55,23,7,6]
common=[]
for i in lst1:
    for j in lst2:
        if(i==j):
            common.append(i)
print("common factors:",common)
"""
