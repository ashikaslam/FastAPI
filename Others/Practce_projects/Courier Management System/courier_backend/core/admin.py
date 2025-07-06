from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Order


class UserAdmin(BaseUserAdmin):
    list_display = ('id','email','role','is_staff')
    fieldsets = (('Permissions', {'fields': ('role',)}),)
admin.site.register(User, UserAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_man', 'status', 'payment_method', 'payment_status', 'created_at')
admin.site.register(Order, OrderAdmin)
