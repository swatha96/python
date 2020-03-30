## dictionary have collection of keys and values
## keys should be unique but values can have duplicates
## using keys - we can access values but using values cant access the keys
## mutable - eg key:value,"number":1,"name":"swe" - called as pair


dictionary={"key":"value","number":1,101:'swe','dup':"swe"}
print(dictionary)
print(type(dictionary)) ## return the type as dict
print(dictionary[101]) ## print the value of key
dictionary['dup']='disan' ## changing the value using key
print(dictionary)
del dictionary['number'] ## delete the pair of the key
print(dictionary)

