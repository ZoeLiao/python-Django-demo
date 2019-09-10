from django.conf.urls import url
from orders import views


urlpatterns = [
    url(
        r'create/$',
        views.order_create,
        name='order_create'
    ),
]
