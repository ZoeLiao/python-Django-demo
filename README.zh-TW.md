# python-Django-demo
練習用 Django 架設購物網站，並用 Boostrap 構建前端
- 使用技術：
    - Django
        - session (TODO)
    - (TODO)[Celery](http://www.celeryproject.org/)
    - (Bootstrap 4.3)[https://getbootstrap.com/]

- 參考資料：https://kknews.cc/zh-tw/code/pe9o3x8.html

## 學習筆記

### 嵌入 Google Map
- 到 [Google Map](https://www.google.com.tw/maps/preview?hl=zh-TW) 輸入地址，複製的 HTML，詳細可參考：[如何將 Google 地圖嵌入網站？](https://medium.com/@zoejoyuliao/%E5%A6%82%E4%BD%95%E5%9C%A8%E7%B6%B2%E7%AB%99%E5%B5%8C%E5%85%A5-google-%E5%9C%B0%E5%9C%96-636d3452b80d)

### Django
- urls
    - url 的順序影響解析順序，由上往下解析
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
- 上下文
- session

- views
    - get_absolute_url
    - reverse
    - @require_POST: 只響應 POST 請求 

### Bootstrap
- px:
    - padding-left, padding-right
    - ex: `px-2`
- mt:
    - margin-top
    - ex: `mt-5`
