FROM python:3.8-slim-buster

RUN apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/gradient-ai/vanilla-llama
WORKDIR vanilla-llama/
RUN pip install -r requirements.txt

COPY models/7B/ ./models/7B 