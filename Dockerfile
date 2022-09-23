FROM python:latest

WORKDIR /app

COPY World_of_Games/* .

RUN pip3 install -r requirements.txt

CMD [ "python3", "MainGame.py"]
