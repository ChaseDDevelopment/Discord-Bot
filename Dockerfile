FROM python:3.9.6-slim-buster
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python bot.py