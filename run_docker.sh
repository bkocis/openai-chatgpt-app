#!/usr/bin/env bash

docker build --tag=openai-chatgpt-app --build-arg OPENAI_API_KEY=$OPENAI_API_KEY .

docker run -p 8080:8080 openai-chatgpt-app
