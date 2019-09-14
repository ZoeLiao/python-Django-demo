from celery import task
from django.core.mail import (
    EmailMultiAlternatives,
    send_mail
)
from django.conf import settings
from django.template.loader import get_template
from django.utils.translation import gettext as _

from orders.models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = _('python-Django-demo - Order nr. {}').format(order.id)

    template = get_template('mail/order.html')
    data = {
        'WEBSITE_URL': settings.WEBSITE_URL,
        'name': order.first_name,
        'id': order.id
    }
    html_email = template.render(data)

    msg = EmailMultiAlternatives(
        subject,
        settings.EMAIL_HOST_USER,
        to=[order.email]
    )
    msg.attach_alternative(html_email, "text/html")
    res = msg.send()
    print('res', res)
