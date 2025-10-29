# 🔹 Array in Python
# Python has two types of "arrays":

# 1. List (built-in, general-purpose)

# 2. array.array (from array module, more memory-efficient, only one data type)


# 1. List (commonly used)
# Ordered, changeable, allows duplicates.

# Defined using [].

my_list = [1, 2, 3, 2]
print(my_list[0])  # Indexing: Output -> 1


# 2. array.array (less common)
# From array module: from array import array

# All elements must be the same data type.

from array import array
my_array = array('i', [1, 2, 3])

# type in google python 3 typecode to see which one of them should you use
