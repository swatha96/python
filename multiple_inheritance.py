c=0
username,password="swetha","swe@123"
class gmail:
    def g_login(self):#baseclass1
        global c
        g_name=input("Enter the gmail user name :")
        g_password=input("Enter the gmail password :")
        if(username == g_name and password == g_password):
            print("YOU HAVE LOGGED IN SUCCESSFULLY")
            c=1
        else:
            print("INCORRECT USER NAME OR PASSWORD")
class facebook:#baseclass1
    def fb_login(self):
        global c
        fb_name=input("Enter the FaceBook user name :")
        fb_password=input("Enter the FaceBook password :")
        if(username == fb_name and password == fb_password):
            print("YOU HAVE LOGGED IN SUCCESSFULLY")
            c=1
        else:
            print("INCORRECT USER NAME OR PASSWORD")
class game(gmail,facebook):#derivedclass- deriving a class from baseclass1 and baseclass2 called multiple inheritance
    def play(self):
        if(c==1):
            print("YOU ARE READY TO START THE GAME")
        else:
            print("SORRY YOU ARE NOT ALLOWED TO START THE GAME\nTRY AGAIN..........")
start=game()
print("YOU CAN START THE GAME VIA GMAIL OR FACEBOOK LOGIN\n...........................................\nCLICK 1 TO START THE GAME VIA GAMIL OR CLICK 2 TO START THE GAME VIA FACEBOOK")
option=int(input("Enter the number 1 or 2:"))
if(option==1):
    start.g_login()
    start.play()
elif(option==2):
    start.fb_login()
    start.play()
else:
    print("invaid option")
