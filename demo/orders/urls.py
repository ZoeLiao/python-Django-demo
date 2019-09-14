from django.urls import path
from orders import views


urlpatterns = [
    path(
        'create/',
        views.order_create,
        name='order_create'
    ),
]
