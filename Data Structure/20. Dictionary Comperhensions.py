values = {}
for x in range(5):
    values[x] = x * 2

values = {x: x*2 for x in range(5)}  # this does the exact same thing as the loop above, which is called comprehension ( in this case for dictionaries)
