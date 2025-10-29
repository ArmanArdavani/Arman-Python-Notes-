# Immutable: You can’t change items after creation.

# Ordered: Items have a defined order.

# Syntax: tuple1 = (1, 2, 3)

# Use Case: When you want a fixed set of values (e.g., coordinates).

person = ("John", 25, "Male")
print(person[0])  # Output: John

numbers = (1, 2, 5, 6)
numbers = 1, 2, 5, 6   #these two are the same

point = (1, 2)
point_addition = (1, 2) + (3, 4)
point_2 = (1, 2) * 3
print(point, point_addition, point_2)

tuple_funtion_use = tuple("hello world")
print(tuple_funtion_use)

tuple_example = (1, 2, 3, 5, 7)
print(tuple_example[1])
print(tuple_example[2:4])

if 10 in tuple_example:
    print("exist")
