items = [
  ("Product1", 10),
  ("Product2", 9 ),  
  ("Product3", 12),
]


prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]              #this line and the line above do the exact same thing, this line is called List comprehension

filtered = list(map(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]       # this is again the same as the line above but with list comprehensions