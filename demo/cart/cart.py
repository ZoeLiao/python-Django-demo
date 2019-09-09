from decimal import Decimal
from django.conf import settings
from shop.modes import Product


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
