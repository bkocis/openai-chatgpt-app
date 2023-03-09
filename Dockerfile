FROM python:3.10-slim-bullseye

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY $OPENAI_API_KEY

ENV DEBIAN_FRONTEND=noninteractive

COPY ./main.py /opt/main.py
COPY ./requirements.txt /opt/requirements.txt

RUN apt-get update
RUN apt-get install python3-dev -y

RUN pip install --upgrade pip && \
    pip install setuptools wheel && \
    pip install -r /opt/requirements.txt

ENV PYTHONPATH /opt
WORKDIR /opt
EXPOSE 8081

CMD ["bokeh", "serve", "--show", "main.py", "--port", "8081"]