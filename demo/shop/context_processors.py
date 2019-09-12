from django.conf import settings


def meta(request):
    return {
        'WEBSITE_URL': settings.WEBSITE_URL,
        'WEBSITE_TITLE': settings.WEBSITE_TITLE,
        'WEBSITE_DESCRIPTION': settings.WEBSITE_DESCRIPTION,
        'WEBSITE_AUTHOR': settings.WEBSITE_AUTHOR
    }
