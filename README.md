# fastapi-sveltekit-starter
A FastAPI based starter/boilerplate: Async SQLAlchemy, Postgres, Sveltekit, pytest

## How to use
You need Python 3 and pip installed locally. Run the cookiecutter command (at least 1.7) and you'll be asked a few prompts.

```bash
pip3 install cookiecutter
cookiecutter https://github.com/urjeetpatel/fastapi-sveltekit-starter.git
```
If you want to keep up to date with upstream changes (i.e. changes in this template), then it's better to use Cruft, which is fully compatible with Cookiecutter.

```bash
pip3 install cruft
cruft create https://github.com/urjeetpatel/fastapi-sveltekit-starter.git
```
Using cruft will generate a metadata file named .cruft.json (don't delete it). Later on you can update to the current version of this cookiecutter and import the changes to your generated project by running this command:

```bash
cruft update
```

## Features
* To be updated

## Features not included
The following features were left out in favour of simplicity:
* Celery/Flower/Redis - Not needed for simple projects, Celery can be easily replaced with [background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).

### Things to do
- [] Setup FastAPI CRUD example
- [] Add pre-commit hooks: Black, isort, flake8, mypy, tslint
- [] Async SQLAlchemy
- [] Create Github action
- [] Dependabot config
- [] Fix docker setup
- [] [Deploy with gunicorn as process manager](https://www.uvicorn.org/deployment/#gunicorn) (recommended for production)
- [] Coverage report in tests
- [] Deployment instructions
