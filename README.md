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

## Send email
- create settings_local.py by `vim demo/settings_local.py`
- input your email information (settings_local.py is an ignored file):
    - `EMAIL_HOST = 'smtp.gmail.com'`
    - `EMAIL_PORT = 587`
    - `EMAIL_HOST_USER = '<your_email>@gmail.com'`
    - `EMAIL_HOST_PASSWORD = '<your_password>'`
- start Celery by the following command

## Celery
- `celery -A demo worker -l info`
