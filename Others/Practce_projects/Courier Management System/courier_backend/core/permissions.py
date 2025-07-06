from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "Authentication credentials were not provided."
            })
        if request.user.role != 'admin':
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "You must be an admin to perform this action."
            })
        return True


class IsDeliveryMan(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "Authentication credentials were not provided."
            })
        if request.user.role != 'delivery_man':
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "You must be a delivery man to perform this action."
            })
        return True


class IsUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "Authentication credentials were not provided."
            })
        if request.user.role != 'user':
            raise PermissionDenied(detail={
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "You must be a user to perform this action."
            })
        return True
