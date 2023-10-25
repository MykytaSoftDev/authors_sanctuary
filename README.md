# Authors Sanctuary Backend

## Adding Virtual Environment

1. Install Virtual Environment in directory 

```bash
$ python -m venv venv
```

2. Activate Virtual Environment

```bash
$ source venv/bin/activate
```

## Installing packages 

1. Install packages in active virtual environment

```bash
$ pip install -r requirements/local.txt
```

## Run app though Docker

1.Build and run containers using **docker compose**:

```bash
$ docker compose -f local.yml up --build -d --remove-orphans
```

## Read API documentation

Run docker containers, then visit [http://localhost:8080/redoc/]

## How to run linters

```bash
$ docker compose -f local.yml exec api black --exclude=migrations .
$ docker compose -f local.yml exec api isort . --skip venv --skip migrations
$ docker compose -f local.yml exec api flake8 .
```

## How to check test coverage

```bash
$ docker compose -f local.yml run --rm api pytest -p no:warnings --cov=. --cov-report html
```

This command will generate htmlcov directory, open htmlcov/index.html to check test coverage