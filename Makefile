
build:
	flake8 --config=.flake8
	@if [ $$? -eq 0 ]; then \
		echo "Linting passed"; \
	else \
		echo "Linting failed"; \
	fi

	pytest
	@if [ $$? -eq 0 ]; then \
		echo "Tests passed"; \
	else \
		echo "Tests failed"; \
	fi
	docker build --tag=openai-chatgpt-app --build-arg OPENAI_API_KEY=${OPENAI_API_KEY} .
	docker run -p 8081:8081 openai-chatgpt-app
run_local:
	docker run -p 8081:8081 openai-chatgpt-app
run_app:
	bokeh serve --show ../openai-chetgpt-app --port 8081
deploy:
	flake8
	pytest
	docker run -dit -p 8081:8081 openai-chatgpt-app
git_push:
	flake8
	pytest
	git add .
	git commit -m "update run via makefile"
	git push