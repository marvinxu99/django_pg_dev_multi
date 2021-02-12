from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

import stripe


def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


def create_checkout_session(request):
    if request.method == 'GET':
        successful_url = request.build_absolute_uri(reverse('scan_n_pay:stripe_success'))
        cancelled_url = request.build_absolute_uri(reverse('scan_n_pay:stripe_cancelled'))
        stripe.api_key = settings.STRIPE_SECRET_KEY

        amount = request.GET.get('amount')

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                # cancel_url=domain_url + 'cancelled/',
                success_url = successful_url + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url = cancelled_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Total Purchase Amount',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': amount,
                    },
                ]
            )
            return JsonResponse({
                    'status': 'S',
                    'sessionId': checkout_session['id']
                })
        except Exception as e:
            return JsonResponse({
                    'status': 'F',
                    'error': str(e)
                })


class SuccessView(TemplateView):
    template_name = 'scan_n_pay/pay_successful.html'


class CancelledView(TemplateView):
    template_name = 'scan_n_pay/pay_cancelled.html'
