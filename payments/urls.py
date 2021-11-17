from .views import *
from django.urls import path

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payments'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
    path('success', SuccessView.as_view(), name='success'), 
    path('cancelled/', CancelledView.as_view(), name='cancelled'), 
    path('webhook/', stripe_webhook, name='webhook'), 
]
