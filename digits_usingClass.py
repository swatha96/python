class digit:
    def do_1digit_oper(self):
        a=n+7
        print("number is added with 7:",a)
    def do_2digit_oper(self):
        a=n**5
        print("the number is to power of 5:",a)
    def do_3digit_oper(self):
        a=int(input("enter the number:"))
        a1=a+n
        print("addition of 2 user inputs:",a1)
objcall=digit()
n=int(input("Enter the number:"))
if(n<=9):
    objcall.do_1digit_oper()
elif(n<=99):
    objcall.do_2digit_oper()
elif(n<=999):
    objcall.do_3digit_oper()
else:
    print("this will work upto 3 digits")
