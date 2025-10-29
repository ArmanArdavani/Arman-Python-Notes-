# 🔹 Dictionary in Python
# A dictionary is an unordered collection of key-value pairs.

# Each key must be unique.

# Defined using {} with key: value format.

my_dict = {"name": "Arman", "age": 16}

#example 
print(my_dict["name"])      # Output: Arman
print(my_dict.get("age"))   # Output: 16


# common operations
my_dict["country"] = "Iran"     # Add new key-value pair
my_dict["age"] = 17             # Update value
del my_dict["name"]             # Delete key
print("age" in my_dict)         # Check if key exists: True


# Loop through dictionary
for key, value in my_dict.items():
    print(key, value)

#another example 
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)   # these two lines are representig two same dictionaries
print(point["x"])
point["y"] = 4   # just changed y value with this
point["z"] = 20  # just added another key and its value 
print(point)

if "a" in point:
    print(point["a"])


# now lets do use a loop with dictionaries
for key in point:
    print(key, point[key])