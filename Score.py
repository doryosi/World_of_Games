from Utils import scores_file_name, bad_return_code


def add_score(difficulty):
    new_points = int(difficulty) * 3 + 5
    try:
        with open(scores_file_name, "r") as score_file:
            old_score = score_file.read()
            new_points += int(old_score)
    except FileNotFoundError:  # if the file doesn't exist
        print(f"{scores_file_name} is missing. File will be created with a new game scores: {new_points}")
    except PermissionError:
        print(f"{bad_return_code} please change the {scores_file_name} permissions")
        exit()
    except ValueError:  # if the file is empty
        print(f"{scores_file_name} is empty, {new_points} will be written")
    except BaseException as e:
        print(f"{bad_return_code}. the following exception occurred {e.args}")
    finally:
        with open(scores_file_name, "w") as score_file:  # Open the file for writing
            score_file.write(str(new_points))  # add the score



