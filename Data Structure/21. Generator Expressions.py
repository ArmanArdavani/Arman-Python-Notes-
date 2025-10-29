values = [x * 2 for x in range(10)]
for x in values:
    print(x)

# if we put paranthesis instead of square bracker in that list comperhension, we are creaing a Generator expression, like this:
values = (x * 2 for x in range(20))


# because generator objects don't store all intems in memory you won't bne abe to get the total number of items you're working with
# but because they take less memoery (e.g mega byets, giga bytse) we are working with large data sets like in range(10000) we use objcet generator to save memory