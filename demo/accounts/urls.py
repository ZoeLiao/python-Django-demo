from django.conf.urls import url

from accounts import views


urlpatterns = [
    url(
        r'^signin/$',
        views.signin,
        name='signin'
    ),
    url(
        r'^profile/$',
        views.profile,
        name='profile'
    )
]
