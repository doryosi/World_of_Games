from GuessGame import play as guess_play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as currency_roulette
from Score import add_score


def check_name(valid_name):  # check if the name contains only characters
    while valid_name.isalpha() is False:
        valid_name = input("please enter a valid name: ")
    else:
        return valid_name


def welcome(name):  # call the check_name function to validate the name and return a message with the valid name
    name = check_name(name)
    name = name.capitalize()
    msg = f"Hello {name} and welcome to the World of Games.\n" \
          f"Here you can find many cool games to play."
    return msg


def choose_game():  # prompt the user to choose a game and return his choice
    while True:
        game = int(input("Please choose a game to play:\n\t"
                         "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\t"
                         "2. Guess Game - guess a number and see if you chose like the computer\n\t"
                         "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n "))
        if game == 1 or game == 2 or game == 3:
            break
        else:
            print("Please insert a number between 1 to 3\n")
    return game


def choose_difficulty():  # prompt the user to choose a difficulty and return his choice
    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1(easy) to 5(Hard): "))
            if not 0 < difficulty < 6:
                print("Please enter a number between 1 to 5\n")
            else:
                return difficulty
        except ValueError as e:
            print(f"{e.args} Please try again")


def load_game():  # call both functions and returns their values
    game = choose_game()
    difficulty = choose_difficulty()
    if game == 1:
        mem_result = memory_play(difficulty)
        if mem_result is True:
            add_score(difficulty)
    elif game == 2:
        guess_result = guess_play(difficulty)
        if guess_result is True:
            add_score(difficulty)
    else:
        cur_result = currency_roulette(difficulty)
        if cur_result is True:
            add_score(difficulty)

