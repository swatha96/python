## unordered data - each and every runtime - the places will change
## there is not fixed index
## set is immutable
## duplicate values are not allowed - it will print one time only


ser={"swe is a good girl",'bad girl',"bad",'girl',5,-5698,5}
print(ser)
print(ser[2]) ## cant print - error : 'set' object is not subscriptable
ser[1]='swetha' ## error - 'set' object does not support item assignment
del ser[2]  ## 'set' object doesn't support item deletion
