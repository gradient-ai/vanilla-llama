FROM python:3.8-slim-buster

RUN apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/gradient-ai/vanilla-llama
WORKDIR vanilla-llama/
RUN pip install -r requirements.txt
COPY models/7B/ ./models/7B
COPY models/tokenizer.model ./models/tokenizer.model
COPY models/tokenizer_checklist.chk ./models/tokenizer_checklist.chk
RUN sed -i "/return TupleNoPrint((self.server_app, self.local_url, self.share_url))/c\        return Tuple((self.server_app, self.local_url, self.share_url))" /usr/local/lib/python3.8/site-packages/gradio/blocks.py

