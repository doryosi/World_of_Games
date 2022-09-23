FROM python:latest

WORKDIR /app

ADD https://github.com/doryosi/World_of_Games/blob/master/ .

RUN pip3 install -r requirements.txt

CMD [ "python3", "MainGame.py"]
