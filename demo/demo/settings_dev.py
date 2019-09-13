import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 開發階段放置自己的靜態文件
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
