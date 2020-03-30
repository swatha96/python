a=input("enter the word:")
word=a.split(" ")
reverse=""
for i in word:
    reverse= i+reverse
reverse=''.join(reversed(reverse))
print(reverse)
