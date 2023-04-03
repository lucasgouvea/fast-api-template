FROM python:3.10.5-alpine as build

WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
 
FROM python:3.10.5-alpine
 
WORKDIR /code
COPY --from=build /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./fast_api_template /code/fast_api_template
COPY ./run.py /code/

EXPOSE 3000

CMD ["python", "run.py"]