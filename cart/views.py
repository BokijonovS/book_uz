from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from .utils import CartAuthenticatedUser
from django.contrib import messages


def cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request).get_cart_info()
        context = {
            'order_items': cart_info['order_items'],
            'cart_total_price': cart_info['cart_total_price'],
            'page_name': 'Cart',
        }
        return render(request, 'cart/cart.html', context)
    else:
        return redirect('login')


def to_cart(request, product_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_id, action)
        page = request.META.get('HTTP_REFERER')
        return redirect(page)
    else:
        return redirect('login')





