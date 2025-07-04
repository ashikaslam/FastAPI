from django.urls import path
from .views import ProductListAPIView

urlpatterns = [
    path('api/products/list/', ProductListAPIView.as_view(), name='product-list'),
]