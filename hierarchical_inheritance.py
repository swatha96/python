c=0
airtel_phone_numbers=[9812217841,8220899427,8754361017,8220830057,9442034454,1234567890,9874563210]
jio_phone_numbers=[9876543210,9988774455,9966332211,8877445566,8855229966,3366998877,7744112255,8855996633,1234566330]
class paytm:
    def welcome(self):
        print("welcome to recharge via paytm")
        print("select networks\n1.airtel\n2.jio")
class airtel(paytm):
    def airtel_plans(self):
        global c
        while(c==0):
            phone_number=int(input("Enter the valid airtel number:"))
            for i in airtel_phone_numbers:
                if(i==phone_number):
                    print(i,"your mob no offer")
                    c=1
                    break
            else:
                print("invalid number")
                c=0
        c==1
        print("offer 1 : RS 900/- for 90days\noffer 2 : RS 500 for 50days\noffer 3 : RS 399 for 42days")
        while(c==1):
            print("Select the plan\n1.RS 900/- for 90days\n2.RS 500 for 50days\n3.RS 399 for 42days\n4.User defined amount\n5.exit")
            number=int(input("enter the plan number :"))
            if(number==1):
                print("rS 900/- for 90days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==2):
                print("RS 500 for 50days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==3):
                print("RS 399 for 42days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==4):
                amount=int(input("Enter the amount which you want to recharge: "))
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==5):
                print("exited... Thank You")
                c=0
            else:
                print("invalid number")
                c=1      
class jio(paytm):
    def jio_plans(self):
        global c
        while(c==0):
            phone_number=int(input("Enter the valid jio number:"))
            for i in jio_phone_numbers:
                if(i==phone_number):
                    print(i,"your mob no offer")
                    c=1
                    break
            else:
                print("invalid number")
                c=0
        c==1
        print("offer 1 : RS 700/- for 90days\noffer 2 : RS 500 for 50days\noffer 3 : RS 285 for 42days")
        while(c==1):
            print("Select the plan\n1.RS 700/- for 90days\n2.RS 500 for 50days\n3.RS 285 for 42days\n4.User defined amount\n5.exit")          
            number=int(input("enter the plan number :"))
            if(number==1):
                print("rS 700/- for 90days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==2):
                print("RS 500 for 50days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==3):
                print("RS 285 for 42days")
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==4):
                amount=int(input("Enter the amount which you want to recharge: "))
                print("bank approval given\nRecharge done Succussfully")
                c=0
            elif(number==5):
                print("exited... Thank You")
                c=0
            else:
                print("invalid input")
                c=1
aobj=airtel()
aobj.welcome()
while(c==0):
    network=int(input("enter 1 for airtel or 2 for jio:"))
    if(network==1):
        aobj.airtel_plans()
        c=1
    elif(network==2):
        jobj=jio()
        jobj.jio_plans()
        c=1
    else:
        print("invalid number")
        c=0


