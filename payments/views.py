from django.core.checks.messages import Error
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import the_app
import stripe
from eseven.models import Detail, OrderItem, Product
import decimal
from django.core.mail import send_mail
from eseven.forms import OrderForm
# Create your views here.

class PaymentView(TemplateView):
    template_name = 'payments.html'

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': the_app.settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = the_app.settings.STRIPE_SECRET_KEY
        try:
            # create new order item and save to database
            # order_item = OrderItem(
            #     code= OrderItem.objects.get_or_create('code'),
            #     quantity=request.GET.get('quantity'),
            #     product=request.GET.get('product'),
            #     total=request.GET.get('total'),
            #     created_at=request.GET.get('created_at'),
            #     updated_at=request.GET.get('updated_at'),
            # )
            # order_item.save()
            # # create new order detail and save to database
            # order_detail = Detail(
            #     code=request.GET.get('code'),
            #     first_name=request.GET.get('first_name'),
            #     last_name=request.GET.get('last_name'),
            #     email=request.GET.get('email'),
            #     address=request.GET.get('address'),
            #     city=request.GET.get('city'),
            #     state=request.GET.get('state'),
            #     country=request.GET.get('country'),
            #     zipcode=request.GET.get('zipcode'),
            #     complete=request.GET.get('complete'),
            #     created_at=request.GET.get('created_at'),
            #     updated_at=request.GET.get('updated_at'),
            # )
            # order_detail.save()
            

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity':1,
                        'currency': 'usd',
                        'amount': 2300,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})



@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = the_app.settings.STRIPE_SECRET_KEY
    endpoint_secret = the_app.settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)


class OrderConfirm(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Detail.objects.filter(code=kwargs['code']).first()
        return context


def post(request):
        order = Detail.objects.filter(transaction_id=request.data['source']).first()
        if not order:
            raise Error('Order not found!')

        order.complete = True
        order.save()

        send_mail(
            subject='Order Completed!',
            message='Order #' + str(order.id) + ' with a total of $' + str(order.admin_revenue) + ' has been completed!',
            from_email= 'from@email.com',
            recipient_list=['a@a.com', 'b@b.com'],
        )
        send_mail(
            subject='Order Completed!',
            message='Your order #' + str(order.id) + ' has been processed!',
            from_email= 'from@email.com',
            recipient_list=[order.email]
        )

        return JsonResponse({
            'success': True,
            "message": "transaction successful!"
        })