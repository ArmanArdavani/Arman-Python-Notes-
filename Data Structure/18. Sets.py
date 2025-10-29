# 🔹 Set in Python
# A set is an unordered collection of unique elements.

# Defined using {} or the set() constructor.

# Cannot contain duplicates.

# Common uses: removing duplicates, checking membership fast.

numbers = [1, 2, 3, 2]
my_set = set(numbers) # this way you converted your list to a set
print(my_set)  # Output: {1, 2, 3}

my_set.add(4)
my_set.remove(2)
print(3 in my_set)  # Membership check


a = {1, 2, 3}
b = {3, 4, 5}

# Union (all elements)
print(a.union(b))   # Output: {1, 2, 3, 4, 5}
print(a | b)        # Same as union

# Intersection (common elements)
print(a.intersection(b))  # Output: {3}
print(a & b)              # Same as intersection

# subtraction 
print(a - b)


a.add(6)
a.remove(2)
print(3 in a)  # Membership check: True or False
