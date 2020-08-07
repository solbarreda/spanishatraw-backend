# Spanish Atraw Backend

## Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv spanishatraw-venv

$ cd spanishatraw-venv

$ source ./bin/activate

$ git clone git@github.com:solbarreda/spanishatraw-backend.git

$ cd spanishatraw-backend

$ pip install -r requirements.txt
```

## Create you `.env` file

- Make a copy of the `.env_DEFAULT` file and replace the values of the variables as needed. The copy should be at the same directory as the `manage.py` file

## Execute the migrations

```bash
$ python manage.py migrate
```

## Run the server

```bash
$ python manage.py runserver 0.0.0.0:8000
```
