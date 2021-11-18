from django.shortcuts import render
from django.shortcuts import render, redirect
from eseven.models import Product
from cart.cart import Cart
from eseven.models import Link
#impor reverse
from django.urls import reverse
# Create your views here.

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart')

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")

def cart_detail(request):
    return reverse(request, 'cart')
