FROM python:latest

WORKDIR /app

COPY * /app/

RUN pip3 install -r requirements.txt

CMD [ "python3", "MainGame.py"]
