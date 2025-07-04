

import stripe
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect, render
from products.models import Product

# stripe.api_key = settings.STRIPE_SECRET_KEY

stripe.api_key = None


class CreateCheckoutSessionView(View):
    def get(self, request,product_id):
        try:
            amount = Product.objects.get(id=product_id).price
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Test Product',
                            },
                            'unit_amount': int(amount),  
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url = request.build_absolute_uri(reverse('success')),
                cancel_url = request.build_absolute_uri(reverse('cancel'))

            )
            return redirect(checkout_session.url)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")
