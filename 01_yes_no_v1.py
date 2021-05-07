instructions = ""
while instructions.lower() != "xxx":
    # Ask user if played before
    instructions = input("Have you played Lucky Unicorn before? ").lower()

    # If yes program continue
    if instructions == "yes" or instructions == "y":
        instructions = "yes"
        print("Program Continues")

    # If no display instructions
    elif instructions == "no" or instructions == "n":
        instructions = "no"
        print("instructions")

    # ask user to enter a valid answer
    else: 
        print("Please answer yes / no ")

    print("you chose {} " .format(instructions))
