FROM python:latest

WORKDIR /app

COPY . .

RUN pip3 install -r Requirements.txt

RUN pip3 install selenium

CMD [ "python3", "MainGame.py"]
