"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import (
    include,
    path
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signout/', auth_views.LogoutView.as_view(), name="signout"),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('social-auth/', include(('social_django.urls', 'social_django'), namespace='social_django')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
]

# 生產環境不應該用 Django 服務靜態文件
if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
