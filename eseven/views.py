from django.shortcuts import render
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
    print(Product.objects.filter(id=1))

class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Cart.objects.all()
        print(context)
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'