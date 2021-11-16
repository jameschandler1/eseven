from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

class PaymentView(TemplateView):
    template_name = 'payments.html'