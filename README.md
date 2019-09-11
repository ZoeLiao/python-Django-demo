# python-Django-demo
- Use Django to build a online shopping site.
- Techniques for building the demo website:
    - Backend:
        - [Django](https://www.djangoproject.com/)
            - session
            - form
            - email
            - i18n (TODO)
            - test (TODO)
        - [Celery](http://www.celeryproject.org/)
            - [flower](https://flower.readthedocs.io/en/latest/)
        - [AGINX](https://nginx.org/en/) (TODO)
        - [Jenkins](https://jenkins.io/zh/) (TODO)
    - Frontend:
        - [Bootstrap 4.3](https://getbootstrap.com/)
    - Database:
        - [SQLite](https://www.sqlite.org/index.html)
        - [redis](https://redis.io/)
    - Cloud platform:
        - [AWS](https://aws.amazon.com/tw/) (TODO)
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
- Create settings_local.py by `vim demo/settings_local.py` (settings_local.py is an ignored file)
- Input your email information in settings_local.py:
    - `EMAIL_HOST = 'smtp.gmail.com'`
    - `EMAIL_PORT = 587`
    - `EMAIL_HOST_USER = '<your_email>@gmail.com'`
    - `EMAIL_HOST_PASSWORD = '<your_password>'`
- start Celery by the following command

## Celery
- Start: `celery -A demo worker -l info`
- Monitor:
    - `celery -A demo flower`
    - Visit [http://localhost:5555](http://localhost:5555)
