# Spanish Atraw Backend

## Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ python3 -m venv spanishatraw-venv

$ cd spanishatraw-venv

* Linux:
  - $ source ./bin/activate

* Windows Powershell:
  - $ .\\Scripts\\activate

$ git clone git@github.com:solbarreda/spanishatraw-backend.git

$ cd spanishatraw-backend

$ pip install -r requirements.txt
```

## Create Database

Execute the following commands

- Create a user: `create user spanishatraw_user with password 'spanishatraw_password';`

- Alter it with superuser permissions: `# alter user spanishatraw_user with superuser;`

- Create the database: `create database spanishatraw_db owner spanishatraw_user encoding 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';`

## Create you `.env` file

- Make a copy of the `.env_DEFAULT` file and replace the values of the variables as needed. The copy should be at the same directory as the `manage.py` file.

- The `DATABASE_URL` variable should be set with the values from the previous step (Create Database), ie.
  `DATABASE_URL=postgres://spanishatraw_user:spanishatraw_password@localhost:5432/spanishatraw_db`

## Execute the migrations

```bash
$ python manage.py migrate
```

## Run the server

```bash
$ python manage.py runserver 0.0.0.0:8000
```

## Create superuser

```bash
$ python manage.py createsuperuser
```
