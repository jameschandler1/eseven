#import django forms
from django import forms
from .models import Order
from django.forms import ModelForm
#import csrf_exempt
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
    def clean_data(self, data):
        data = super(OrderForm, self).clean()
        return data