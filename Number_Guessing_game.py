import random
#Function to check users' guess against actual answer

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining...."""
    if user_guess>actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess<actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")



#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS





def game():
    #choosing a random number between 1 to 100...
    choice = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    guess = 0
    while guess!= choice:

        print(f"You have {turns} attempts remaining t guess the number. ")



        #let the user guess  a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, choice,turns)
        if turns == 0:
            print("You've run out of guesses, you lose. ")
            return
        elif guess!= choice:
            print("Guess again. ")

    #track the number of turns and reduce by 1 if the get it wrong....
    #Repeat the guessing functionality if they get it wrong..

game()


