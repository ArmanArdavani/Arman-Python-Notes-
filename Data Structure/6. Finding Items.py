letters = ["a", "b", "c"]

print(letters.index("a")) # we use the index funtion to use find the index of the items we are looking for in a list
letters.count("d")        # this will give the number of occurences of the given item in this list

if "d" in letters:
    print(letters.index("d"))


