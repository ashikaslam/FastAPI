# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('create-checkout-session/<int:order_id>/',CreateCheckoutSessionAPIView.as_view(), name='create_checkout_session'),
    path('success/',payment_success, name='success'),
    path('cancel/',payment_cancel, name='cancel'),
]
