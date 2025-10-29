# 🔹 For Loop in Python
# A for loop is used to iterate over a sequence (like a list, string, tuple, set, or dictionary).

# for item in sequence:  sequence should be an iterable like lists, string, tuple, set or dictionary. when we say range of something that is somethings like lists too.)
    # do something with item

numbers = [1, 2, 3]
for num in numbers:   # it essentially gets every item in the sequnce of numbers in that list and executes the thing that you asked from it (E.g here when say multiply it by 2, num*2)
    print(num * 2)
    
# Output: 1 2 3







#First case for loops
for number in range(5):
    print("won")
print("done")

#Second case 
for number in range(5):
    print("won", number)
print("1st case done")
 
#Third case
for number in range(10):
    print("won", number+1)
print("2nd case done")

#Fourth case(same results as past case)
for number in range(1,10):
    print("won",number)
print("3rd case done")

#Fifth case 
for number in range(1,10):
    print("won",number,(number)* ".")
print("4th case done")

#Sixth Case (the third number in the range makes the numbers add up by that number)
for number in range(1,10,3):
    print("won",number,(number)*".")
print("5th case done")