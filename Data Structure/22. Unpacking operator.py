values_1 = list(range(5))      # this turns the range of (0,4) to a list of [0, 1, 2, 3, 4], which as we know ranges are iterables as well 
values = [*range(5), *"hello"] # this way we are unpacking the range of (0,5) and also unpacking the string heloo
print(values)

# we can combine two lists with this unpacking method as well 
first = [1,2]
second = [3, 4]
combination = [*first, *second]
print(combination)

# we can unpack dictionaries as well but we need to use two asterisks:
first_2 = {"x": 1}
second_2 = {"x": 10, "y": 2}
combined = {**first_2, **second_2, "z": 2}
print(combined)