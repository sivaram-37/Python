#Product of all elements in the list

from functools import reduce
li=[1,2,3,4]
prod=reduce(lambda a,b:a*b,li)
print(prod)