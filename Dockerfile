FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY Pipfile /code
COPY Pipfile.lock /code
RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --three --system --deploy --sequential --verbose
COPY * /code/