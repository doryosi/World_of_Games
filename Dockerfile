FROM python:latest

WORKDIR /app

COPY . .

RUN pip3 install -r Requirements.txt

RUN ls -l

CMD [ "python3", "MainGame.py"]
