numbers = [3, 51, 2, 8, 6] 
numbers.sort() # this way we sort the itmes in a list 
print(numbers)

numbers.sort(reverse=True)  # this way we can reversaly sort our list 
print(numbers)

print(sorted(numbers)) # this is the 2nd way 
print(sorted(numbers, reverse=True))


items = [
  ("Product1", 10),
  ("Product2", 9 ),  
  ("Product3", 12),
]
items.sort()
print(items) # this way of sorting is not going to work right now, because it cannot identify that we want to srouc based on the 2nd item of the touple

def sort_item(item):  # so this way we are definning a function that gets an item in the list of items and give the index[1] of the touple which is the number price in this case 
    return item[1]

items.sort(key=sort_item)
print(items)