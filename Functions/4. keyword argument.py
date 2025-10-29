def increment(number, by):
    return number + by


result = increment(3,2)
print(result)


# we can simplify this code like this (in line 6)

def increment_2(number, by):
    return number + by


print(increment_2(2,3))

#if we want to make our code more readable we can show the paramters value which are the arguments like this
def increment_3(number, by):
    return number + by 


print(increment_3(number=2, by=3))