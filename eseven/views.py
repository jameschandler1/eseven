from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
#import  generic TemplateView
from django.views.generic import TemplateView
#import DetailView
from django.views.generic.detail import DetailView
#import all models
from .models import *



# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class ProductListView(TemplateView):
    template_name = 'products_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        print(Product.objects.all())
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    

# def add_to_cart(request, product_id, code):
#     product = get_object_or_404(Product, pk=product_id)
#     cart, created = Cart.objects.get_or_create(code=code, active=True)
#     order, created = OrderItem.objects.get_or_create(cart=cart, product=product)
#     order.quantity += 1
#     order.save()
#     messages.success(request, 'Item added to cart')
    
#     return redirect('cart')

class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Cart.objects.all()
        print(context)
        return context



class ContactView(TemplateView):
    template_name = 'contact.html'



