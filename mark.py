english_mark=int(input("enter the mark in english subject :"))
science_mark=int(input("enter the mark in science subject :"))
maths_mark=int(input("enter the mark in mathematics subject :"))
total=(english_mark+science_mark+maths_mark)
print("Your total marks:",total)
percentage=int(total/3)
print("Your percentage is:",percentage)
if percentage>=80:
    print("you got distinction")
elif percentage>=60:
    print("you got first class")
elif percentage>=45:
    print("you got second class")
elif percentage>=35:
    print("you have passed")
else:
    print("you failed")

