"""
name=input("enter your first name:")
sur_name=input("enter your surName:")
number=len(name)
if number<=6:
    number=int(number/2+1)
else:
    number=int(number/2)
names=""
for i in range(number):
    names=name[i]+names
names=''.join(reversed(names))
print(names,sur_name[0].upper())
"""


name=input("enter your first name:")
sur_name=input("enter your surName:")
number=len(name)
number=int(number/2+1)
names=""
for i in range(number):
    names=name[i]+names
names=''.join(reversed(names))
print(names,sur_name[0].upper())


 
