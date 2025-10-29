#lambda function format 
# name_of_our_function = key=lambda parameter: return

# for example
def square_area(x):
    return x**2

print(square_area(8))

# if we turn it into lambda is:
square_area = key=lambda x: x**2
print(square_area(5))
#--------------------------------------------
#another example
def add(a, b):
    return a + b 
print(add(3, 4))

addition = key=lambda a, b: a+b
print(addition(5, 6))
#--------------------------------------------

items = [
  ("Product1", 10),
  ("Product2", 9 ),  
  ("Product3", 12),
]
items.sort()
print(items) 

def sort_item(item):  
    return item[1]
                      
items.sort(key=lambda item:item[1]) #this way we are defining a function in a shorter way, we used lambda function to write the upper function in a faster way
print(items)


