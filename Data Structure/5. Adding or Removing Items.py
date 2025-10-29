letters = ["a", "b", "c"]

# Add
letters.append("d")    # to add to the end of the List
letters.insert(0, "-") # to add to the beginning of the lis

print(letters)

# Remove 
letters.pop()       # this Removes "d" from the list which is at the end of the list 
letters.pop(0)      # with this we remove the letter we want at the given index 
letters.remove("b") # this will remove the given string in the bracket. but if you have mutipule of those strings you need to creat a loop to remove all of them to remove with this.
del letters[0:3]    # with del function we can remove indexes and a range of indexes
letters.clear()     # we use this to remove all the items of the list
print(letters)