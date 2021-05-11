# function
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If yes program continue
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        # ask user to enter a valid answer
        else: 
            print("Please answer yes / no ")


def instructions () :

    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False 
    while not valid:
        try:
            # question
            response = int(input(question))

            # if the amount is too low or too high
            if low < response <= high:
                return response


            # output an error
            else:
                print(error)
        
        except ValueError:
            print(error)

# Main Routine
show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()

print("Program Continues")
print()

# Ask user how much they want to play with
how_much = num_check ("How much would you like to play with? ", 0, 10)


print("You will be spending ${}" .format(how_much))

