#import django forms
from django import forms

from django.forms import ModelForm
#import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from .models import Detail

@csrf_exempt
class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"

class OrderForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'