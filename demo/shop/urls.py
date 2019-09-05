from django.conf.urls import url

from shop import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(
        r'^(?P<category_slug>[-\W]+)/$',
        views.product_list,
        name='product_list_by_category'
    ),
    url(
        r'^(?P<id>\d+)/(?P<slug>[-\W]+)/$',
        views.product_detail,
        name='product_detail'
    )
]
