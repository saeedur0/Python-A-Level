#bubble sort

items = ["saeedur","abdul","nafis","armaan","haris","umar" ]

n = len(items)
swapped = True

while n > 0 and swapped == True:
    swapped = False
    n = n - 1
    for index in range (0,n):
        if items[index] > items[index+1]:
            tempvar = items[index]
            items[index]= items[index+1]
            items[index+1] = tempvar
            swapped = True

print(items)



