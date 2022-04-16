from random import randint
from time import sleep


def generate_sequence(diff):  # generate a list of numbers according to the difficulty
    list_numbers = []
    for number in range(diff):
        random_num = randint(1, 101)
        list_numbers.append(random_num)
    return list_numbers


def show_sequence(seq):  # show the list of numbers for 0.7 seconds
    print(seq)
    sleep(0.7)
    print(chr(27) + "[2J")


def get_list_from_user(diff):  # ask the user for a list of numbers
    user_list = []
    for number in range(diff):
        while True:
            try:
                user_number = int(input(f"Guess the {number + 1} number between 1 to 101: "))
                if 1 < user_number < 101:
                    user_list.append(user_number)
                    break
                else:
                    print(f"the {user_number} isn't between 1 to 101\nplease try again")
            except ValueError as e:
                print(f"{e.args}\nplease try again")
    return user_list


def is_list_equal(list_numbers, user_list):  # check whether the user was correct or incorrect
    if list_numbers == user_list:
        return True
    else:
        return False


def play(diff):  # call all the functions of the games and declares if the user won or lost
    list_numbers = generate_sequence(diff)
    show_sequence(list_numbers)
    user_list = get_list_from_user(diff)
    result = is_list_equal(list_numbers, user_list)
    if result is True:
        print(f"You Won!!!\nThe {list_numbers} is the same as {user_list}")
        return True
    else:
        print(f"You Lost!!!\nThe {list_numbers} is not the same as {user_list}")
        return False
