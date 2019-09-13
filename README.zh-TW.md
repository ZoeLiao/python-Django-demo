# python-Django-demo
![demo_homepage_zh_Hant.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_homepage_zh_Hant.png)
- [English (英文)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.md)
- 這是一個用 Django 與 Bootstrap 架設的 demo 購物網站的的倉庫
- 使用技術：
    - 後端：
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
        - [AGINX](https://nginx.org/en/) (TODO)
        - [Jenkins](https://jenkins.io/zh/) (TODO)
    - 前端:
        - [Bootstrap (4.3)](https://getbootstrap.com/)
    - 資料庫:
        - [SQLite](https://www.sqlite.org/index.html)
    - 緩存：
        - [Redis](https://redis.io/)
    - 雲端服務:
        - [AWS](https://aws.amazon.com/tw/) (TODO)

- 參考資料：https://kknews.cc/zh-tw/code/pe9o3x8.html

## 學習筆記

### Medium 筆記
- 嵌入 Google Map：
    - 到 [Google Map](https://www.google.com.tw/maps/preview?hl=zh-TW) 輸入地址，複製的 HTML，詳細可參考 Medium 筆記：[如何將 Google 地圖嵌入網站？](https://medium.com/@zoejoyuliao/%E5%A6%82%E4%BD%95%E5%9C%A8%E7%B6%B2%E7%AB%99%E5%B5%8C%E5%85%A5-google-%E5%9C%B0%E5%9C%96-636d3452b80d)

- Django + Celery + Redis + Gmail 實現異步寄信：
    - 可參考 Medium 筆記：[Django + Celery + Redis + Gmail 實現異步寄信](https://medium.com/@zoejoyuliao/django-celery-redis-gmail-%E5%AF%84%E4%BF%A1-375904d4224c)

- Django 國際化：

### Django
- urls
    - url 的順序影響解析順序，由上往下解析
    - path V.S url ?
    - i18n
- settings
    - STATICFILES_DIRS 與 STATIC_ROOT：
        - 開發階段放置自己的靜態文件  
        `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
        - 執行 collectatic 後會將項目中的靜態文件收集到此目錄下
        `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
    - media
        - MEDIA_URL = '/media/'

- templates
    - filter:
        - linebreaks
            - {{ value|linebreaks }}，若 value='Joel\nis a slug'，則渲染完後為：<p>Joel<br>is a slug</p>
    - i18n
    - static
- 上下文
- session
- form.as_p
- csrf_token

- views
    - get_absolute_url
    - reverse
    - @require_POST: 只響應 POST 請求 

### Bootstrap
- 元素的邊界設定：
    - px:
        - padding-left, padding-right
        - ex: `px-1`
    - py:
        - padding-top, padding-top
        - ex: `py-2`
    - mt:
        - margin-top
        - ex: `mt-3`
    - mb:
        - margin-bottom
        - ex: `mb-4`
