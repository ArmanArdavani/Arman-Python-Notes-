letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]  # martix is a two dimensional list

zeros = [0] * 5            # this wil allow me now to print a list with 5 zeros 
print(zeros) 

combined = zeros + letters # here we are adding these two list to be in one list 
print(combined)

numbers = list(range(20)) # here we are using list function and range (loop) to create a list of number 0 up to 20
print(numbers)

chars = list("Hello World") # because strings are iterable as well, we can put strings into the input of list functioin as well 
print(chars)  
print(len(chars))           