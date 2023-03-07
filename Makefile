
build:
	docker build --tag=openai-chatgpt-app --build-arg OPENAI_API_KEY=${OPENAI_API_KEY} .
run:
	docker run -p 8080:8080 openai-chatgpt-app
deploy:
	docker run -dit -p 8080:8080 openai-chatgpt-app