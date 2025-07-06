from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, User
from .serializers import (
    OrderSerializer,
    RegisterSerializer,
)

from .permissions import IsAdmin, IsDeliveryMan, IsUser




class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_serializer_context(self):
        return {'request': self.request}


class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_queryset(self):
        return Order.objects.filter()




class DeliveryManOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsDeliveryMan]
    def get_queryset(self):
        return Order.objects.filter(delivery_man=self.request.user)

class DeliveryManOrderStatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDeliveryMan]

    def get(self, request, order_id, status_value):
        print(request.user.role)
        valid_statuses = ['pending', 'assigned', 'delivered', 'complete']
        if status_value not in valid_statuses:
            return Response({
                "success": False,
                "message": f"Invalid status '{status_value}'. Must be one of: {valid_statuses}"
            }, status=status.HTTP_400_BAD_REQUEST)

        delivery_man = request.user
        order = get_object_or_404(Order, id=order_id, delivery_man=delivery_man)

        order.status = status_value
        order.save()

        return Response({
            "success": True,
            "message": "Order status updated successfully.",
            "order_id": order.id,
            "status": order.status
        }, status=status.HTTP_200_OK)


class AdminOrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class AdminAssignDeliveryManView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    def get(self,request,order_id,deliveryman_id):
        print("hello",' ',order_id,' ',deliveryman_id)
        order = get_object_or_404(Order, id=order_id)
        delivery_man = get_object_or_404(User,id=deliveryman_id, role='delivery_man')

        order.delivery_man = delivery_man
        order.status = 'assigned'
        order.save()

        return Response({
            "success": True,
            "message": f"Delivery man (ID: {deliveryman_id}) assigned to order (ID: {order_id}).",
            "order_id": order.id,
            "delivery_man": delivery_man.email,
            "status": order.status
        }, status=status.HTTP_200_OK)




