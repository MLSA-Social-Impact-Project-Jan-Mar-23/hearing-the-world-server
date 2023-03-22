FROM python:3.10.10-slim-buster AS builder

RUN pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock ./
COPY . .

FROM builder AS DEV
RUN pipenv install --dev
CMD ["pipenv","run","dev"]

FROM builder AS PROD
RUN pipenv install
CMD ["pipenv","run","prod"]
