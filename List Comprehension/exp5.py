# create a new list to store elements that are palindrome from a given list

mylist=['radar','racecar','python']
pali_li=[i for i in mylist if list(i)==list(reversed(list(i)))]
print(pali_li)