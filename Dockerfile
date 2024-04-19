FROM python:alpine

WORKDIR /wordfreqana

COPY . /wordfreqana/

RUN pip install nltk

CMD python wordfreq.py