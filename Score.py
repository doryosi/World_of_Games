from Utils import scores_file_name, bad_return_code


def add_score(difficulty):
    added_score = difficulty * 3 + 5
    try:
        with open(scores_file_name, "r+") as f:
            file_content = f.read(1)
            if not file_content:  # if the file is empty
                f.write(str(added_score))
                return added_score
            else:  # if the file is not empty
                f.seek(0)  # go to the beginning of the file
                old_score = f.read()  # read all of its content
                new_score = added_score + int(old_score)  # add the old score to the new score
                f.seek(0)  # go to the beginning of the file again
                f.truncate()  # remove the content within the file
                f.write(str(new_score))  # add the new score
                return new_score
    except FileNotFoundError:  # if the file doesn't exist
        with open(scores_file_name, "w") as f:  # create it
            f.write(str(added_score))  # add the score
            return added_score
    except PermissionError:
        print(f"{bad_return_code}please change the file permission")
    except BaseException as e:
        print(bad_return_code + e.args)


add_score(4)


