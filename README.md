# python-Django-demo
- Use Django to build a online shopping site.
- Techniques for building the website:
    - [Django](https://www.djangoproject.com/)
        - session
        - form
    - (TODO)[Celery](http://www.celeryproject.org/)
    - [Bootstrap 4.3](https://getbootstrap.com/)
- [中文 (Traditional Chinese)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.zh-TW.md)

## Start project
- `python3 -m venv venv`
- `django-admin startproject <project_name>`
- `django-admin startapp <app_name>`

## Set Up
- `virtualenv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`
- `cd demo`
- `export PYTHONPATH=$PWD`
- `python manage.py migrate`
- `python manage.py createsuperuser`

## Migrate Database
- `python manage.py makemigrations`
- `python manage.py migrate`
