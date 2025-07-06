from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from core.models import Order
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY  





class CreateCheckoutSessionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # optional, depending on your needs

    def get(self, request, order_id):
        print("helo here???")
        try:
            order = get_object_or_404(Order, id=order_id)

            if order. payment_status=='Paid':
                return Response({
                    "success": False,
                    "message": "This order is already paid."
                }, status=status.HTTP_400_BAD_REQUEST)

            amount = int(order.cost_ammount)

            success_url = request.build_absolute_uri(
                reverse('success') + f"?order_id={order.id}"
            )
            cancel_url = request.build_absolute_uri(reverse('cancel'))

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': f"Order #{order.id}",
                            },
                            'unit_amount': amount,
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
            )

            return Response({
                "success": True,
                "checkout_url": checkout_session.url,
                "message": "Stripe checkout session created."
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




def payment_success(request):# Success view dev only — for prod  we have to use ipn or  webhooks 
    order_id = request.GET.get("order_id")
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            order.payment_status = 'Paid'
            order.save()
        except Order.DoesNotExist:
            pass  
    return render(request, "success.html", {"order_id": order_id})



def payment_cancel(request):
    return render(request, "cancel.html")
