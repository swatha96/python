"""
without class:
..............

c=0
while(c==0):
    number=int(input("enter the number:"))
    if(number==5):
        for i in range(0,5):
            print(i)
            print(i)
            print(i)
            print(i)
        break
    elif(number==3):
        for i in range(0,3):
            print(i)
            print(i)
        break
    else:
        c==0
.................
Using class:
............
"""
class five_three:
    def five(self):
        for i in range(5):
            print(i)
            print(i)
            print(i)
            print(i)
    def three(self):
        for i in range(0,3):
            print(i)
            print(i)
obj=five_three()
c=0
while(c==0):
    number=int(input("enter the number:"))
    if(number==5):
        obj.five()
        c=1
    elif(number==3):
        obj.three()
        c=1
    else:
        c=0
