FROM python:3.10-slim-bullseye

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY $OPENAI_API_KEY

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /opt/openai-chatgpt-app

COPY ./templates /opt/openai-chatgpt-app/templates
COPY ./main.py /opt/openai-chatgpt-app/main.py
COPY ./requirements.txt /opt/openai-chatgpt-app/requirements.txt

RUN apt-get update
RUN apt-get install python3-dev -y

RUN pip install --upgrade pip && \
    pip install setuptools wheel && \
    pip install -r /opt/openai-chatgpt-app/requirements.txt

ENV PYTHONPATH /opt
WORKDIR /opt
EXPOSE 8081

CMD ["bokeh", "serve", "openai-chatgpt-app", "--port", "8081", "--show"]