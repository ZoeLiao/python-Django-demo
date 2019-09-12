from django.conf import settings


def meta(request):
    return {'WEBSITE_URL': settings.WEBSITE_URL}
