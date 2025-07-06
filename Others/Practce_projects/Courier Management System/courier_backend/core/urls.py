from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from .views import *
urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/create/', CreateOrderView.as_view(), name='create-order'),
    path('orders/user/', UserOrderListView.as_view(), name='user-orders'),
    path('orders/admin/', AdminOrderListView.as_view(), name='admin-orders'),
    path('orders/admin/assign/<int:order_id>/<int:deliveryman_id>/', AdminAssignDeliveryManView.as_view(), name='assign-delivery-man'),
    path('orders/delivery/', DeliveryManOrderListView.as_view(), name='deliveryman-orders'),
    path('delivery/update-status/<int:order_id>/<str:status_value>/', DeliveryManOrderStatusUpdateView.as_view(), name='update-order-status'),
]
