
from django.urls import path
from . views import *
from cart.views import * 
from payments.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category', ProductCatListView.as_view(), name='category'),
    path('tops', TopsView.as_view(), name='tops'),
    path('bottoms', BottomsView.as_view(), name='bottoms'),
    path('accessories', AccessoriesView.as_view(), name='accessories'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products_details'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/', contact, name='contact_form'),
    path('cart', CartView.as_view(), name='cart'),
    path('cart', cart_detail, name='cart_detail'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
]
