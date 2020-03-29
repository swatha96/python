SBI_Balance,ICICI_Balance=27500,45892
transfer_amount=0
c=0
class SBI:#baseclass
    def check(self):
        print("SBI balance :",SBI_Balance)
class gpay(SBI):#intermediate class derived from baseclass
    def transer(self):
        global transfer_amount,c
        transfer_amount=int(input("Enter the amount which you want to transfer:"))
        if(transfer_amount<=SBI_Balance):
            print("Amount transfered to ICICI Bank\nACCOUNT BALANCE BEFORE TRANSFER :",SBI_Balance,"\nCURRENT ACCOUNT BALANCE:",SBI_Balance-transfer_amount,"\n............................")
            c=1
        else:
            print("There is no sufficient balance in the Bank Account\n..................................")
class ICICI(gpay):#derived class derived from intermediatev class
    def deposit(self):
        print("Credit received from SBI Bank\nACCOUNT BALANCE BEFORE TRANSFER :",ICICI_Balance,"\nCURRENT ACCOUNT BALANCE:",ICICI_Balance+transfer_amount,"\n............................")
transfer=ICICI()
transfer.check()
transfer.transer()
if(c==1):
    transfer.deposit()
else:
    print("Thanks for choosing SBI")

        
        
