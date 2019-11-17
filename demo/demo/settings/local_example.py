import os
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# send an order email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your_gmail>'
EMAIL_HOST_PASSWORD = '<your_password>'

# sign in with 3-party accounts
## Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '<your_fb_key>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your_fb_secret>'

## Instagram
SOCIAL_AUTH_INSTAGRAM_KEY = '<your_ig_key>'
SOCIAL_AUTH_INSTAGRAM_SECRET = '<your_ig_secret>'

## Github
SOCIAL_AUTH_GITHUB_KEY = '<your_github_key>'
SOCIAL_AUTH_GITHUB_SECRET = '<your_github_secret>'

# Use MySQL or sqlite3
## MySQL
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': '<your_user>',
#        'NAME': '<your_name>',
#        'PASSWORD': '<your_pwd>',
#        'HOST': '<your_host>',
#        'PORT': '3306',
#    }
#}

## sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
