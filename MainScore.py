from flask import Flask, render_template
from Utils import scores_file_name, bad_return_code
import webbrowser


app = Flask("something")


@app.route('/')
def score_server():
    try:
        with open(scores_file_name) as f:
            score = f.read()
            return render_template('score.html', score=score)
    except BaseException as e:
        return render_template('score_error.html', bad_return_code=bad_return_code, error=e.args)


def start_server():
    app.run(host="0.0.0.0", port=5003)




