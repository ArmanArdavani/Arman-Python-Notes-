numbers = [1, 2, 3] 

first = numbers[0]
second = numbers[1]
third = numbers[2]

# we can do this in a more efficient way 

first, second, third = numbers
print(first, second, third)

numbers_2 = [1 ,2 ,3 ,4 ,4 ,4 ,4 ,4]
first, second, *other = numbers_2
print(first)
print(other)


numbers_3 = [1, 2, 3, 4, 4, 4, 9]
first, *other, last = numbers_3
print(first)
print(*other)
print(last)