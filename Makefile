virtual_env:
	poetry config virtualenvs.in-project true
install:
	poetry install
run:
	poetry run start