FROM python:latest

# Prerequisites
RUN apt-get -y update
RUN apt-get install -y libnss3

# From https://www.2daygeek.com/install-google-chrome-browser-on-linux/
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN pip install webdriver_manager

# Passing arguments
ARG PROJ_NAME
ARG PORT
ENV PROJ_NAME World_of_Games
ENV PORT 5000

WORKDIR /World_of_Games
COPY Scores.txt /World_of_Games
COPY *.py /World_of_Games/
COPY tests/e2e.py /World_of_Games/
COPY ./templates/* /World_of_Games/templates/
COPY Requirements.txt /World_of_Games/Requirements.txt
RUN pip3 install -r /World_of_Games/Requirements.txt
EXPOSE 5000
CMD [ "python3", "MainScore.py"]
