FROM python:latest

WORKDIR /app

COPY Scores.txt .
COPY *.py .
COPY Requirements.txt .

RUN pip3 install -r Requirements.txt

CMD [ "python3", "MainScores.py"]
