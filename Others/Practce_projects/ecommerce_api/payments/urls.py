# urls.py

from django.urls import path
from .views import success, cancel, CreateCheckoutSessionView

urlpatterns = [
    path('create-checkout-session/<int:product_id>/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]
