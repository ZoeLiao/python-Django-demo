from demo.settings.base import *


# 開發階段放置自己的靜態文件
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    # import email information
    from demo.settings.local import *
except ImportError:
    pass
