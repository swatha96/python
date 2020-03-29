number=int(input("enter thr number:"))
class digit:
    def digit0(self):
        print("enter the number :")
    def digit1(self):
        print("single digit number")
    def digit2(self):
        print("double digit number")
    def digit3(self):
        print("3 digits number")
    def digit4(self):
        print("4 digits number")
    def digit5(self):
        print("5 digits number")
    def digit6(self):
        print("6 digits number")
    def digit7(self):
        print("7 digits number")
    def digit8(self):
        print("8 digits number")
    def digit9(self):
        print("9 digits number")
            
obj=digit()          
if number == 0:
    obj.digit0()
elif number<=9:
    obj.digit1()
elif number<=99:
    obj.digit2()
elif number<=999:
    obj.digit3()
elif number<=9999:
    obj.digit4()
elif number<=99999:
    obj.digit5()
elif number<=999999:
    obj.digit6()
elif number<=9999999:
    obj.digit7()
elif number<=99999999:
    obj.digit8()
elif number<=999999999:
    obj.digit9()
else:
    print("number limit exceeded")
