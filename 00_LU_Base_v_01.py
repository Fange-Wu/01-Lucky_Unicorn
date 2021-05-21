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
    print()
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10). \n \n Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn. \n \n It costs a $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts... \n Unicorn: $5.00 (balance increase by $4) \n Horse: $0.50 (balance decreases by $0.50) \n Zebra: $0.50 (balance decrease by $0.50) \n Donkey: $0.00 (balance decrease by $1.00) \n \n (type <xxx> to quit)")
    print()
    statement_generator("Let's get Started...", "-")
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


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

    
# Main Routine
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()

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
        prize_decoration = "!"
    
    # if the random # is between 6 and 46
    # user will get donkey *minus 1$ from balance
    elif 6 <= chosen_num <=36 :
        chosen = "donkey"
        balance -= 1
        prize_decoration = "D"
    
    # if the token is either horse or zebra 
    # minus $0.50 from the balance
    else:
        # if number is even token = horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # if odd number user will get zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5
    
    outcome = "You got a {}. Your balance is " "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        statement_generator("Sorry you have run out of money", "V")
    else:
        play_again = input("Press <Enter> to play or <xxx> to quit ")
    

print()
statement_generator("Results", "=")
print("Final Balance $",balance)
print("Thank you for playing")


