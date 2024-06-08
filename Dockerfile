FROM python:latest

# Prerequisites
RUN apt-get -y update

RUN apt-get install -y libnss3

WORKDIR /World_of_Games

COPY Scores.txt /World_of_Games

COPY *.py /World_of_Games/

COPY ./templates/* /World_of_Games/templates/

COPY Requirements.txt /World_of_Games/Requirements.txt

RUN pip3 install -r /World_of_Games/Requirements.txt

EXPOSE 5000

CMD [ "python3", "MainScore.py"]
