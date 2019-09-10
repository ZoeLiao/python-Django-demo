from django.conf.urls import url
from cart import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'add/(?P<product_id>\d+)/$',
        views.cart_add,
        name='cart_add'
    ),
    url(r'remove/(?P<product_id>\d+)/$',
        views.cart_remove,
        name='cart_remove'
    ),
]
