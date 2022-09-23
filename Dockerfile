FROM python:latest

WORKDIR /app

COPY . .

RUN pip3 install -r Requirements.txt

CMD [ "python3", "MainGame.py", "99999"]
