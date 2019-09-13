import os

DEBUG = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 執行 collectatic 後會將項目中的靜態文件收集到此目錄下
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
