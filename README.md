# python-Django-demo
![demo_homepgae_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_homepage_en.png)
- [繁體中文 (Traditional Chinese)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.zh-TW.md)
- Use Django to build an online demo shopping site.
- Functions:
    - Basic shopping site
    - Able to sign in with third-party accounts (Facebook, Instagram, Github)
    - Use session to record user's cart
    - Sending email by Celery + Redis + Gmail
    - Internationalization
    - Deploy: AWS + Docker + uWSGI + Nginx
- Techniques & tools for building the demo website:
    - Backend:
        - [Django (2.2)](https://www.djangoproject.com/)
            - social-auth-app-django (Facebook, Instagram, Github)
            - session
            - form
            - email
            - management
            - i18n
            - test (TODO: finish)
        - [Celery](http://www.celeryproject.org/)
            - [flower](https://flower.readthedocs.io/en/latest/)
        - [Docker](https://www.docker.com/)
        - [AGINX](https://nginx.org/en/)
        - [Jenkins](https://jenkins.io/zh/) (TODO)
    - Frontend:
        - [Bootstrap (4.3)](https://getbootstrap.com/)
    - Database:
        - [SQLite](https://www.sqlite.org/index.html)
    - Cache:
        - [Redis](https://redis.io/)
    - Cloud platform:
        - [AWS](https://aws.amazon.com/tw/) (TODO)
- Reference:
    - [shopping site (中文)](https://kknews.cc/zh-tw/code/pe9o3x8.html)
    - [Loggin in with social media accounts](https://scotch.io/tutorials/django-authentication-with-facebook-instagram-and-linkedin)
    - [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)

## Set up
- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`
- `cd demo`
- `export PYTHONPATH=$PWD`
- `python manage.py migrate`
- `python manage.py createsuperuser`

## Start an app
- If you want to add a new funtion:
    - `django-admin startapp <app_name>`

## Migrate database
- In general cases:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- Failed to detect changes:
    - Run the command of [Management - Delete the data of specific app](https://github.com/ZoeLiao/python-Django-demo#management)
    - fake:
        - Tells Django to mark the migrations as having been applied or unapplied, but without actually running the SQL to change your database schema
        - `python manage.py makemigrations <app_name>`
        - `python manage.py migrate --fake`
    - migrate:
        - `python manage.py makemigrations <app_name>`
        - `python manage.py migrate`

## Management
- Delete the data of specific app:
    - `python manage.py manual_migration <app_name>`
    - ex: `python manage.py manual_migration shop`

## Static files
- `python manage.py collectstatic`

## Send emails
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

## Test
- `python manage.py test <app_name>.tests`

## i18n
- `python manage.py makemessages -l zh_Hant`
- `python manage.py compilemessages`

## Docker
- `mkdir <path>/sites-available`
- Build: `docker-compose up --build`
- Run: `docker-compose up`
- Remove: `docker-compose down -v`
- docker system prune (-f)
- AWS:
    - `docker-compose up -d`
    - `sudo usermod -a -G docker $USER`
    - sign out and sign in again
    - `sudo service docker start`

## Deploy
- `python manage.py collectstatic`
- No apt-get: `mkdir /etc/nginx/sites-available/`
- `docker-compose up --build`
- `python manage.py migrate`
