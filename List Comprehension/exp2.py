# create a new list to store that the elements are Odd or Even from a given list

mylist=[1,2,3,5]
l1=["Even" if i%2==0 else "Odd" for i in mylist]
print(l1)