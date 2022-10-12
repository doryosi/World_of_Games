from flask import Flask, render_template
from Utils import scores_file_name, bad_return_code


app = Flask("User Score")


@app.route('/')
def score_server():
    try:
        with open(scores_file_name) as f:
            score = f.read()
        if '' == score:
            raise IOError(f"The {scores_file_name} is empty!")
        if not score.isnumeric():
            raise IOError(f"{scores_file_name} isn't a number {score}")
        else:
            return render_template('score.html', score=score)
    except BaseException as e:
        return render_template('score_error.html', bad_return_code=bad_return_code, error=e.args)


app.run(host="0.0.0.0", port=5001, debug=False)




