def increment(number, by=3):
    return number+by


print(increment(2))
# now here even tho we didn't gave the 2nd argument, because the value of the 2nd parametr was defind at first, the programm will put it as that 

def increment_2(number, by=3):
    return number + by


print(increment_2(2,5))

# but now altough we gave a value to the parameter at first, but because now we added another value for the parameter "by" in the argument as well,
# the programm will put it as the argument valie