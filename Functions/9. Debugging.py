def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number 
        return total         # we deliberately ceated this bug in our programm to debugg it. return should be at the lvel of "for" 
                             # we use put a break point for debugging on one line, then with F5 start the debugging, with F10 go to the next line 
                             # and with F11 come back up to the first line of function

print("Start")
print(multiply(1, 2, 3)) 