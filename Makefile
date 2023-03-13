port=8082
app_name=openai-chatgpt-app

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
	docker build --tag=${app_name} --build-arg OPENAI_API_KEY=${OPENAI_API_KEY} .
	docker run -p ${port}:${port} ${app_name}
run_local:
	docker run -p ${port}:${port} ${app_name}
run_app:
	bokeh serve --show ../${app_name} --port ${port}
deploy:
	docker build --tag=${app_name} --build-arg OPENAI_API_KEY=${OPENAI_API_KEY} .
	docker run -dit -p ${port}:${port} ${app_name}
git_push:
	flake8
	pytest
	git add .
	git commit -m "update run via makefile"
	git push
