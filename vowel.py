vowel=["a","A","e","E","i","I","o","O","u","U"]
c=0
letter=input("enter the single letter in alphabet:")
for i in vowel:
    if i==letter:
        print("the letter is vowel",letter)
        c=1
if c==0:
    print("the letter is consonant",letter)

"""
using if condition:

letter=input("enter the single letter in alphabet:")
if(letter == "a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U"):
    print("the letter is vowel",letter)
else:
    print("it's consonant")
"""
