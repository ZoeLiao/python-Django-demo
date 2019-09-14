from django.db import models
from shop.models import Product
import django.utils.timezone as timezone
from django.utils.translation import gettext_lazy


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=gettext_lazy('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=gettext_lazy('Last Name'))
    email = models.EmailField(verbose_name=gettext_lazy('Email'))
    address = models.CharField(max_length=250, verbose_name=gettext_lazy('address'))
    postal_code = models.CharField(max_length=20, verbose_name=gettext_lazy('postal_code'))
    city = models.CharField(max_length=100, verbose_name=gettext_lazy('city'))
    created_at = models.DateTimeField(
            default = timezone.now
        )
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
            Order,
            related_name='items',
            on_delete=models.CASCADE
    )
    product = models.ForeignKey(
            Product,
            related_name='order_items',
            on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
