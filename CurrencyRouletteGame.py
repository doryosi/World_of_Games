import requests
from random import randint


def get_rate():  # get the ILS-USD rate from API
    url = "http://api.currencylayer.com/live?access_key=d836c538c86aa8b2219b6e7355ffe507"
    response = requests.get(url)
    data = response.json()
    usd_ils_rate = data["quotes"]["USDILS"]
    return usd_ils_rate


def get_money_interval():  # generate a rand num
    rand_num = randint(1, 100)
    return rand_num


def get_ils_amount(usd_ils_rate, rand_num):  # calculate the correct answer
    ils_amount = rand_num * usd_ils_rate
    return ils_amount


def get_guess_from_user(rand_num):  # get the user guess for the generated amount of dollars
    while True:
        try:
            user_guess = int(input(f"How much ILS will you get for {rand_num} dollars: "))
            if user_guess is int:
                break
            break
        except ValueError as e:
            print(e.args)
    return user_guess


def decide_range(diff, ils_amount):  # decide the range based on the difficulty and the correct answer
    up_range = round(ils_amount + (5 - diff))
    down_range = round(ils_amount - (5 - diff))
    return down_range, up_range


def play(diff):  # call all the functions and declares whether the user won or lost
    random_interval = get_money_interval()
    rate = get_rate()
    correct = get_ils_amount(rate, random_interval)
    user_guess = get_guess_from_user(random_interval)
    valid_range = decide_range(diff, correct)
    if valid_range[0] <= user_guess <= valid_range[1]:
        print(f"You Won\nYour guess is {user_guess}, between the range: {valid_range[0]} - {valid_range[1]}")
        return True
    else:
        print(f"You Lost\nYour guess is {user_guess}, not between the range: {valid_range[0]} - {valid_range[1]}")
        return False











