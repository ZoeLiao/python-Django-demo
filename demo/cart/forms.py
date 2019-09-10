# -*- coding: UTF-8 -*-
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # 用戶可以在 PRODUCT_QUANTITY_CHOICES 的範圍內選擇數量
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int
            )
    update = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.HiddenInput
            )

