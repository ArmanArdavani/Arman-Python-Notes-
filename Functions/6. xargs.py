def multiply(*numbers):
    print(numbers)


multiply(3,4,6,7)

print("1st Case done")




def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number    #this line means total = total * number, so its like multiplying the total by each of the numbers in the argument
    return total     


print(multiply(3,4,5,6))  # with this code we are multiplying 3,4,5,6 

print("2nd case Done")
#in this example with used a combination of funtion with loops to get the product of these numbers in the argument