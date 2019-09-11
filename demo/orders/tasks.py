from celery import task
from django.core.mail import send_mail
from django.conf import settings

from orders.models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [order.email]
    )
    return mail_sent
