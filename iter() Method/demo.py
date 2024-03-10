
li=[10,20,30,40,50,60]
res=iter(li)

# print(next(res))
# print(next(res))

# or
# to display all elements of the list

while True:
    try:
        print(next(res))
    except:
        break