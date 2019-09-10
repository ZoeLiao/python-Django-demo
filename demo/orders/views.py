from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=oder,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )

            cart.clear()
            return render(
                request,
                'orders/order/created.html',
                {'order': order}
            )
    else:
        form = OrderCreateForm()
    return render(
        request,
        'orders/order/create.html',
        {
            'cart': cart,
            'form': form
        }
    )
