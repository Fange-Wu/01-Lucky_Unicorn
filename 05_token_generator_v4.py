import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE


# Testing loop to genereate 20 tokens
for item in range (0,10) :
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
    
print()
print()
print("Starting Balance: ${:.2f}" .format(STARTING_BALANCE))
print("Final Balance: ${:.2f}" .format(balance))