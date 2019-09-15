from django.urls import path

from shop import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('list', views.product_list, name='product_list'),
    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),
    path(
        '<int:id>/<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),
]
