# # create a new list to store only digit of each elements from a given list

mylist=['ab12','cd34','gf56']
digit=[j for i in mylist for j in i if j.isdigit()]
print(digit)