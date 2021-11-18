from django.core.checks.messages import Error
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import the_app
import stripe
from eseven.models import Order, Product, OrderItem, Link
import decimal
from django.core.mail import send_mail
from eseven.forms import OrderForm
# Create your views here.


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': the_app.settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

class PaymentView(TemplateView):
    template_name = 'payments.html'

@csrf_exempt
def create_checkout_session(request):
    domain_url = 'https://e7vintage.herokuapp.com'
    stripe.api_key = the_app.settings.STRIPE_SECRET_KEY
    if request.method == 'GET':
        order = Order()
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order.save()
    # link = Link.objects.filter(code__icontains='code').first()
        for item in request.session['cart']:
            product = Product.objects.filter(id=item)
            order_item = OrderItem(
                order=order, 
                product_title=request.session['cart'][item]['name'], 
                price=request.session['cart'][item]['price'], 
                quantity=request.session['cart'][item]['quantity']
            )
        del request.session['cart']

    line_items = []

    line_items.append({
        'name': order_item.product_title,
        'amount': (100 * order_item.price),
        'currency': 'usd',
        'quantity': order_item.quantity
    })
        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
    checkout_session = stripe.checkout.Session.create(
        success_url=domain_url + '/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=domain_url + 'cancelled/',
        payment_method_types=['card'],
        mode='payment',
        line_items=line_items,
    )
    return JsonResponse({'sessionId': checkout_session['id']})



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
        context['order'] = Order.objects.filter(code=kwargs['code']).first()
        return context


def post(request):
        order = Order.objects.filter(transaction_id=request.data['source']).first()
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