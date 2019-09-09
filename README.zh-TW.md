# python-Django-demo
練習用 Django 架設購物網站
- 使用技術：
    - Django
        - session (TODO)
    - Bootstrap (TODO)
    - Celery (TODO)

- 參考資料：https://kknews.cc/zh-tw/code/pe9o3x8.html

## 學習筆記
### Django
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

- views
    - get_absolute_url
    - reverse

### Bootstrap
- px:
    - padding-left, padding-right
    - ex: `px-2`
- mt:
    - margin-top
    - ex: `mt-5`
