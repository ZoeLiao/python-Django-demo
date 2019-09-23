# -*- coding: UTF-8 -*-
from django.shortcuts import (
    render,
    get_object_or_404
)
from shop.models import (
    Category,
    Product
)
from cart.forms import CartAddProductForm


def homepage(request):
    categories = Category.objects.all()
    return render(
        request,
        'shop/homepage.html',
        {
            'categories': categories
        }
    )

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products
        }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(
            Product,
            id=id,
            slug=slug,
            available=True
        )
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {
            'product': product,
            'cart_product_form': cart_product_form
        }
    )


def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__contains=query)
    else:
        products = Product.objects.filter(available=True)
    category = None
    categories = Category.objects.all()
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
            'query': query
        }
    )
