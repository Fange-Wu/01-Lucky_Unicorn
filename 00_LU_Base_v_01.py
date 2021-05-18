import random

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
    error = "Please enter a whole number between 1 and 10\n"

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

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play... ").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number 
    print()
    print("*** Round #{} ***".format(rounds_played))
   
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5 
    # user will get unicorn *add 4$ to balance
    if 1 <= chosen_num <=5 :
        chosen = "unicorn"
        balance += 4
    
    # if the random # is between 6 and 46
    # user will get donkey *minus 1$ from balance
    elif 6 <= chosen_num <=36 :
        chosen = "donkey"
        balance -= 1
    
    # if the token is either horse or zebra 
    # minus $0.50 from the balance
    else:
        # if number is even token = horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # if odd number user will get zebra
        else:
            chosen = "zebra"
        balance -= 0.5
    
    print("You got a {}.  Your balance is ${:.2f} " .format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press <Enter> to play or <xxx> to quit ")
    

print()
print("Final Balance $", balance)


