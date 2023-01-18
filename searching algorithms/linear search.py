#linear search

array = ['saeedur','success','islam','allah']
print(array)
item_find = input("enter item to find ")

found = False
index = 0

while found == False and index < len(array):
    if array[index] == item_find:
        found = True
    else:
        index = index + 1

if found == True:
    print('item has been found at position', index)
else:
    print("item not found") 