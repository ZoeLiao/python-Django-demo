# -*- coding: UTF-8 -*-
from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart():
    def __init__(self, request):
        """
        Initialize the cart to set the session
        """
        # 將 request 對象初始化
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        product_price = str(product.price)
        quantity = int(quantity)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': product_price
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """
        Update cart
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        # 標記 session 告訴 Django 已經改動，需要保存
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id) 
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_id = str(product.id) 
            self.cart[product_id]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def claer(self):
        """
        Empty the cart
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
