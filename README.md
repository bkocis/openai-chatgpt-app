###
[![Python application](https://github.com/bkocis/openai-chatgpt-app/actions/workflows/python-app.yml/badge.svg)](https://github.com/bkocis/openai-chatgpt-app/actions/workflows/python-app.yml)
------------------------------------------------------------------------------------------------------------------------

#### Python web application using OpenAI ChatGPT API

This Github repository contains a web application built using the Bokeh framework. The Bokeh framework is used to 
generate a simple frontend for the web app, which can be easily customized as per user requirements.

##### Dockerized App

The web app is dockerized, making it easy to deploy and run on different platforms. 
Dockerizing the app also ensures that it is independent of the underlying platform, making it highly portable.

##### OpenAI API Key

For this application a OpenAI API key is required. The API key can be obtained by signing up for a paid account at [OpenAI API keys](https://platform.openai.com/account/api-keys).

In order to run the web app, you will need to pass the OpenAI API key to the Docker build command from the environment 
variable. This ensures that the app can access the OpenAI API and perform the necessary tasks.



##### Build and Run

To build and run the app, simply use the `make build && make run_local` command, or `make deploy` to run the docker container 
 in detached mode, which means that the container runs in the background and the console is released to the user for other activities.

Thank you for checking out our project. 
Please feel free to submit any issues or pull requests to help us improve the app.