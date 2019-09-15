# python-Django-demo
- [繁體中文 (Traditional Chinese)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.zh-TW.md)
- Use Django & Bootstrap to build an online demo shopping site and deploy on AWS.
- Demo Website: [https://zoeliao.nctu.me](https://zoeliao.nctu.me) (account: root, passowrd: admin)
- Images: 
    - homepage  
    ![demo_homepgae_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_homepage_en.png)
    - products  
    ![demo_products_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_products_en.png)
    - no product  
    ![demo_no_image_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_no_image_en.png)
    - detail  
    ![demo_detail_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_detail_en.png)
    - cart  
    ![demo_carts_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_carts_en.png)
    - checkout  
    ![demo_checkout_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_checkout_en.png)
    - share  
    ![demo_share_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_share_en.png)
    - order confirmation email  
    ![demo_mail.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_mail.png)
    - login  
    ![demo_3parts_login_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_3parts_login_en.png)
    - login - github  
    ![demo_3parts_login_github_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_3parts_login_github_en.png)
    - demo map  
    ![demo_map_en.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_map_en.png)

- Functions:
    - Support to:
        - Add goods to shopping cart (recorded by session),
        - Send order confirmation email to customers (Celery + Redis + Gmail),
        - Sign in with third-party accounts (Facebook, Instagram, Github),
        - Share to Facebook
        - View address on Google Map
        - Manage Categories and Goods in the admin interface.
    - Responsive web design (RWD).
    - Internationalization (i18n).
    - Deployment (AWS + Docker + uWSGI + Nginx + Cerbot).
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
    - Frontend:
        - [Bootstrap (4.3)](https://getbootstrap.com/)
    - Database:
        - [SQLite](https://www.sqlite.org/index.html)
    - Cache:
        - [Redis](https://redis.io/)
    - Deployment:
        - [AWS](https://aws.amazon.com/tw/)
        - [Docker](https://www.docker.com/)
        - [AGINX](https://nginx.org/en/)
        - [Certbot (Let's encryp)](https://certbot.eff.org/)
        - [Jenkins](https://jenkins.io/zh/) (TODO)
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
- Input your email information in demo/settings/local.py:
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
- container:
    - `docker container ls`
    - `docker exec -it <Container ID> bash`

## Deployment
- `docker-compose up --build`
- `docker exec -it <Web Container ID> bash`
- `python manage.py collectstatic`
- `python manage.py createsuperuser`

## Git
- Git doesn't notice change in image:
    - `git rm --cached path/to/image.jpg`
