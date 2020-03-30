## string is immutable (cant change the value)
## enclosed with single or double Quote'' or "" for group of strings { }

## if we have not enclosing the values - defaultly it will take as a tuple even its number or string

str="56" ## it will take as string
str2='swetha'
print(type(str))  ## it will return str
print(type(str2))
print(str2[3]) ## it will print 3rd index
del str2[1]  ## 'str' object doesn't support item deletion



s="asd",'swe','swe is a good girl',5,5
d=5,5,6,9,10
print(d) ##  will print enclosed with parenthesis- it will considered as type tuple
print(d[4])
print(type(d)) ## return type as tuple
print(s) ## will print enclosed with parenthesis- it will considered as type tuple
print(s[2])
print(type(s)) ## return - tuple
del s[1]   ##  error :'tuple' object doesn't support item deletion




