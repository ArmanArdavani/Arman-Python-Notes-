# here we are trying to give an input as a user which is the command and the answer we get is going to be in the format, Arman + the command
# but if the command is equal to quit, the infinite loop is going to "break" and stop.
while True:
    command = input(">")
    print("Arman", command)
    if command.lower() == "quit":
        break