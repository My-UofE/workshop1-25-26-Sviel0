import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    num = len(poss_values)//2
    x = poss_values[num]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val:
        if user_input == "l":
            return True
        elif user_input == "h":
            return False
    elif current_val < next_val:
        if user_input == "l":
            return False
        elif user_input == "h":
            return True
        

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    guess = 0
    for x in range(len(board)):
        if letter == word[x]:
            guess += 1
            board[x] = letter
    if guess == 0:
        print(f"Sorry, '{letter}' is not in the word")
        return False
    elif guess > 0:
        print(f"Well done! '{letter}' is in the word")
        return True
            

