from demo.settings.base import *


DEBUG = False

# 執行 collectatic 後會將項目中的靜態文件收集到此目錄下
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

WEBSITE_URL = 'https://zoeliao.nctu.me'

# Import from local
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '3306',
#    }
#}


try:
    # import email information
    from demo.settings.local import *
except ImportError:
    pass
