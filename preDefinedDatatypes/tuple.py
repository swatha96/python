## tuple is immutable(cant change)
## its have index starts from 0
## enclosed with parenthesis () - defaultly it will take as tuple
## it can have duplicate value


tup=(56,'swe',89,5,0,-6,'A','b',89)
t=56,5,'swe'
print(type(t)) ## it will return as tuple
print(tup)
print(type(tup)) ## it will return datatype as tuple
print(tup[3]) ## print3rd index - 4th value
tup[6]=45  ## cant assign (error : does not support item assignment)
del tup[2] ## cant del (error : 'tuple' object does not support item deletion)




s="asd",'swe','swe is a good girl',5,5
d=5,5,6,9,10
print(d) ##  will print enclosed with parenthesis- it will considered as type tuple
print(d[4])
print(type(d)) ## return type as tuple
print(s) ## will print enclosed with parenthesis- it will considered as type tuple
print(s[2])
print(type(s)) ## return - tuple
del s[1]   ##  error :'tuple' object doesn't support item deletion

