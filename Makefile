virtual_env:
	poetry config virtualenvs.in-project true
install:
	poetry install
run:
	poetry run python run.py
build:
	docker build . --no-cache -t fast-api-template
run-c:
	docker run -p 3000:3000 fast-api-template