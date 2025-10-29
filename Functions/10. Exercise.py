# we have an algorithme. --> if we give input divisible by 3 it gives "Fizz" 
# if we give input divisible by 5 it give buzz
# and if its both divisible by 3 and 5 it gives FizzBuzz
# and if the input was not divisible by 3 nor 5 it returns the input itself 

#this was my first solution
def fizz_buzz(input):
    if input % 3 == 0:
        print("fizz")
    elif input % 5 == 0:
        print("buzz")
    elif input % 3 == 0 and input % 5 == 0:
        print("Fizz_buzz")
    else:
        print(input)

    print(fizz_buzz(3))


#this is the main correct solution

def fizz_buzz2(input):
    if (input % 3 == 0 ) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input          # here its like sayin else: return the input, but because we didn't use elif and that format we can just write it like this.

print(fizz_buzz2(45))