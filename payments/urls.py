from .views import *
from django.urls import path

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payments'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session),
    path('success', SuccessView.as_view()), # new
    path('cancelled/', CancelledView.as_view()), # new
    path('webhook/', stripe_webhook),
]
