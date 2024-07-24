# when sorting tuples, we need to convert them to lists first
tuple_1 = (1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 0, -1, -2, -3, -4, -5)

# convert to list and sort
temp = list(tuple_1)
temp.sort()
print(temp)

# resign the sorted value back to tuple_1
tuple_1 = tuple(temp)
print(tuple_1)

