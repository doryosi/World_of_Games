import os
scores_file_name = "Scores.txt"
bad_return_code = -1
success_return_code = 0


def screen_cleaner():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

