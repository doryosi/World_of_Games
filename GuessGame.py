from random import randint


# Receives the user difficulty and generate a random number between 1 and the chosen difficulty
def generate_number(user_difficulty):
    secret_number = randint(1, user_difficulty)
    return secret_number


# Prompts the user to insert a number
def get_guess_from_user(user_difficulty):
    while True:
        try:
            user_num = int(input(f"Enter a number between 1 to {user_difficulty}: "))
            if 1 < user_num <= user_difficulty:
                return user_num
        except ValueError as e:
            print(f"{e.args} Please try again")


# Compare between the secret number and the user number
def compare_results(secret_number, user_number):
    if user_number == secret_number:
        return True
    else:
        return False


# Calls all the functions and prints whether the user guessed the right number or not
def play(diff):
    secret_number = generate_number(diff)
    user_number = get_guess_from_user(diff)
    start_the_game = compare_results(secret_number, user_number)
    if start_the_game is True:
        print(f"You Won, the secret number was {secret_number}")
        return True
    else:
        print(f"You Lost, the secret number was {secret_number}")
        return False
