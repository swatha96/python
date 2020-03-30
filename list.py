## list is mutable(change)
## its have index starts from 0
## enclosed with [ ]
##it can have duplicate value

lst=[56,'swe',89,5,0,-6,'A','b',89]
print(type(lst))## it will return type as a list
print(lst)
del lst[2] ## delete index 2- 3rd value
print(lst)
print(lst[4]) ## print only 4th index
lst[5]=45 ## changing the value of 5th index
print(lst)
