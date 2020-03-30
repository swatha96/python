##type conversion
## we cant mutate some datatypes such as tuple, string etc...
## to mutate those datatypes using type converting or type casting
## change the immutable datatype to mutable datatype(list)
## we can convert from tuple, string into list and we can reconvert into string or tuple after task completed.
## we cant directly convert from list to string or tuple, set .....


str1='swe is a girl' ## string
print(type(str))
lst=list(str1)   ## converting from string to list
print(lst)
print(type(lst))
lst.remove(" ")  ## remove - using value,,, here we have deleted a space - it will delete first space - it cant delete multi values
print(lst)
lst.pop(5)  ## delete index 5- it cant delete multi index
print(lst)
s=str(lst)
print(s,type(s)) ## recovert


tup1=1,'swe',-1,-1,0,"good",896,'swe is a girl'
tup2=(2,"swe",'swe',-9,634)
print(type(tup1),type(tup2))
lst1,lst2=list(tup1),list(tup2)
print(type(lst1),type(lst2))
lst1.insert(2,"man")   ## added a value in list using index - here in 2nd index we have added
print(lst1)   
t=tuple(lst1)
print(type(t)) ## reconvert

