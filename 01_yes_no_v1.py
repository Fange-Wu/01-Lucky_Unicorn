# Ask user if played before
instructions = input("Have you played Lucky Unicorn before? ").lower()

# If yes program continue
if instructions == "yes" or "y":
    print("Program Continues")

# If no display instructions
elif instructions == "no" or "n":
    print("instructions")

# ask user to enter a valid answer
else: 
    print("Please answer yes / no ")

