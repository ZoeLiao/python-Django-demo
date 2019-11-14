# python-Django-demo
- [English README.md (英文 README.md)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.md)
- 這是一個用 Django、Bootstrap、MySQL、Celery、Redis、Docker 架設並部署在 AWS 的購物網站。
- Demo 網址：[https://zoeliao.nctu.me](https://zoeliao.nctu.me) (管理介面帳號：root，密碼：admin)（因為沒有要找工作所以下線了）
![demo_homepage_zh_Hant.png](https://raw.githubusercontent.com/ZoeLiao/python-Django-demo/zoeliao/dev/demo/static/images/demo_homepage_zh_Hant.png)
- 功能：
    - 支持：
        - 第三方登入 (Facebook、Instagram、Github)、
        - 將商品加入購物車並提交訂單 (session)、
        - 異步發送訂單確認電子郵件給客戶 (Celery + Redis + Gmail)、
        - 分享到 Facebook、
        - 查看 Google 地圖、
        - 後台管理商品清單。
    - 響應式網站設計 (RWD)。
    - 國際化 (i18n)。
    - 部署 (AWS + Docker + uWSGI + NGINX + Certbot)。
- 使用技術與工具：
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
    - 前端:
        - [Bootstrap (4.3)](https://getbootstrap.com/)
        - [Google Analytics (gtag.js)](https://developers.google.com/analytics/devguides/collection/gtagjs)
    - 資料庫:
        - [MySQL](https://www.mysql.com/)
    - 緩存：
        - [Redis](https://redis.io/)
    - 部署:
        - [AWS](https://aws.amazon.com/tw/)
        - [Docker](https://www.docker.com/)
        - [AGINX](https://nginx.org/en/)
        - [Certbot (Let's encryp)](https://certbot.eff.org/)
        - [Jenkins](https://jenkins.io/zh/) (TODO)

- 展示圖片與程式指令請查看：[English READEM.md (英文 README.md)](https://github.com/ZoeLiao/python-Django-demo/blob/master/README.md)
- 參考資料：
    - [shopping site (中文)](https://kknews.cc/zh-tw/code/pe9o3x8.html)
    - [Loggin in with social media accounts](https://scotch.io/tutorials/django-authentication-with-facebook-instagram-and-linkedin)
    - [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)

## Medium 筆記
- [如何將 Google 地圖嵌入網站？](https://medium.com/@zoejoyuliao/%E5%A6%82%E4%BD%95%E5%9C%A8%E7%B6%B2%E7%AB%99%E5%B5%8C%E5%85%A5-google-%E5%9C%B0%E5%9C%96-636d3452b80d)
- [Django + Celery + Redis + Gmail 實現異步寄信](https://medium.com/@zoejoyuliao/django-celery-redis-gmail-%E5%AF%84%E4%BF%A1-375904d4224c)
- [Django 國際化（一）- 在 template 、views、models 新增 i18n 標籤生成 .po & .mo 檔](https://medium.com/@zoejoyuliao/django-%E5%9C%8B%E9%9A%9B%E5%8C%96-i18n-%E4%B8%80-%E5%9C%A8-template-%E6%96%B0%E5%A2%9E-i18n-%E6%A8%99%E7%B1%A4%E7%94%9F%E6%88%90-po-mo-%E6%AA%94-1d41f2fcfc78)
- [磁盤空間不足 (No space left on device)](https://medium.com/@zoejoyuliao/%E7%A3%81%E7%9B%A4%E7%A9%BA%E9%96%93%E4%B8%8D%E8%B6%B3-no-space-left-on-device-b31da374a865)
- [Plug your Django application logging directly into AWS CloudWatch](https://medium.com/@zoejoyuliao/plug-your-django-application-logging-directly-into-aws-cloudwatch-d2ec67898c0b)

## 其他筆記
### Django
- urls：
    - url 的順序影響解析順序，由上往下解析。
    - path V.S url ?：
        - Django 2.0 以前用 url，2.2 雖然支持，但建議改用 path 以及 re_path (== url)
        - path 支持定義類型：int, str, slug, uuid，如：`path(/order/<int:num>/, views.order, name='order')`
- settings：
    - STATICFILES_DIRS 與 STATIC_ROOT：
        - 開發階段放置自己的靜態文件
        `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
        - 執行 collectatic 後會將項目中的靜態文件收集到此目錄下
        `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`

- templates：
    - filter：
        - linebreaks
            - {{ value|linebreaks }}，若 value='Joel\nis a slug'，則渲染完後為：<p>Joel<br>is a slug</p>
- context_processors：
    - 上下文渲染器，為函數返回字典，可以用於每個 request 返回的模板。
- form.as_p：
    - 將 form 渲染出來。
- csrf_token：
    - CSRF (Cross-Site Request Forgery，跨站請求攻擊，跨站偽造請求），Django 發送 POST 請求時需要驗證，前端要加 `{% csrf_token %}` 以避免跨站請求的問題。參考資料：[Python Tutorial 第五堂（2）表單與 CSRF](http://www.codedata.com.tw/python/python-tutorial-the-5th-class-2-form-csrf/)

- views：
    - get_absolute_url：
        - 在 model 定義 url 與對象一一對應的關係。
    - reverse：
        - 避免在 template 硬編碼 url。
    - @require_POST：
        - 只響應 POST 請求

### Bootstrap
- 元素的邊界設定：
    - px：
        - padding-left, padding-right
        - ex： `px-1`
    - py：
        - padding-top, padding-bottom
        - ex：`py-2`
    - mt：
        - margin-top
        - ex：`mt-3`
    - mb：
        - margin-bottom
        - ex：`mb-4`
- flexbox：
    - Bootstrap 4 以後開始用 flexbox 而不是 floats 來管理 layout。
    - row：
        - 左右 (x軸)
    - col：
        - 上下 (y軸)
    - align-self：
        - 自身移動 - start、end、center、baseline、stretch
    - 網格系統 (container - row - col) 本身具有 flex 屬性不用加。
    - 無網格系統可用 ```d-flex``` 和 ```d-inline-flex``` 來創建 flexbox。
## 部署：
- Django + Docker + NGINX + uWSGI：
    - [twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)
- HTTPS 管理：
    - 域名申請：
        - [NCTU Domain免費網域申請教學](https://medium.com/@NorthBei/nctu-domain%E5%85%8D%E8%B2%BB%E7%B6%B2%E5%9F%9F%E7%94%B3%E8%AB%8B%E6%95%99%E5%AD%B8-b629fdaaad90)
    - [Certbot (Let's encryp)](https://certbot.eff.org/)
    - [解析 Certbot（Let's encrypt） 使用方式](https://andyyou.github.io/2019/04/13/how-to-use-certbot/)
