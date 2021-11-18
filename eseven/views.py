from django.http import response
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
#import  generic TemplateView
from django.views.generic import TemplateView
#import DetailView
from django.views.generic.detail import DetailView

#import all models
from .models import *
#import all forms
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
#import get_template
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class ProductListView(TemplateView):
    template_name = 'products_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_image(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.Product.objects.filter('image')
        return context
    
class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        print(context)
        return context
        
class ContactView(TemplateView):
    template_name = 'contact.html'

    @csrf_exempt
    def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = request.POST.get('subject')
                contact_name = request.POST.get('name', '')
                contact_email = request.POST.get('email', '')
                form_message = request.POST.get('message', '')
                form_message = request.POST.get('message', '')

                # Email the profile with the contact information
                template = get_template('contact_template.txt')
                context = {
                    'subject': subject,
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_message': form_message,
                }
                content = template.render(context)

                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + '',
                    ['stillsound@protonmail.com'],
                    headers = {'Reply-To': contact_email}
                )
                email.send()
                return redirect('contact')

        return render(request, 'contact.html', {'form': form})

