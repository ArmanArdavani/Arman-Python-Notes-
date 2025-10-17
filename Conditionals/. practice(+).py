# here we have a exercise, you should write a code that shows even numbers from 2 to 8 with using this for range funtion: rang(1,10)
# and at the end part it should print we have 4 even numbers

count_of_even_numbers = 4 
for number in  range (1, 10):
    if number //2 == number/2:
        print(number)  
print("we have", count_of_even_numbers, "even number") 

# this was my own answer that i got that says for the numbers in range 1 to 10, if we divide them by 2
# their real answer(with decimals) is going to  be equal to the only the whole number answer of the division


#here is the full completed answer

count_even_numbers = 0
for number in range(1, 10):
    if number % 2 == 0:
        count_even_numbers += 1  # here we are saying each time that the if statement was true, add 1 to the initail count_even_number varibale, Thus 0 + (1*4) = 4
        print(number)
print(f"we have {count_even_numbers} even numbers")
 
# here we used the modulus(%) to say if the remaining of the division by two is zero you print it
# and if count of even numbers are bigger or equal to 1, we used formmated string to print "we have this amout of even numbers"

