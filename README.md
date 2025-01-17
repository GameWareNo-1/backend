# GoCardless sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/GameWareNo-1/backend.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(.venv)$ pip install -r requirements.txt
```
Note the `(.venv)` in front of the prompt. This indicates that this terminal

Once `pip` has finished downloading the dependencies make migrations and migrate:
```sh
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py migrate
```
Finally run the server
```sh
(.venv)$ python manage.py runserver
```