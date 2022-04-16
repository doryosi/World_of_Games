from flask import Flask
from Utils import scores_file_name

app = Flask("something")


@app.route('/')
def score_server():
    try:
        with open(scores_file_name) as f:
            score = f.read()
            return f'<h1>The score is <div id="score">{score}</div></h1>'
    except BaseException as e:
        return f'<h1><div id="score" style="color:red">{e.args}</div></h1>'


app.run(host="0.0.0.0", port=5003, debug=True)