# django3.1.1-simple-template
Django 3.1.1 simple website template

## Install requirements (need Python 3.7)
```
python -m venv env
```
### Windows
```
env/Scripts/activate
```
### Linux
```
env/bin/activate
```
### In virtual env:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run website
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Server available on http://127.0.0.1:8000/

After work deactivate virtual env
