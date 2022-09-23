FROM python:latest

WORKDIR /app

COPY . .

RUN ls -l

RUN pip3 install -r requirements.txt

CMD [ "python3", "MainGame.py"]
