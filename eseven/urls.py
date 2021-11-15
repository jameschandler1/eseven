
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products', ProductListView.as_view(), name='products'),
    path('products/<str:pk>', ProductDetailView.as_view(), name='products_details'),
    path('cart', CartView.as_view(), name='cart'),
    path('contact', ContactView.as_view(), name='contact'),
]