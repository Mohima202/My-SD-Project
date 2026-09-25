from django.contrib import admin
from .models import SignupData, CartItem, Order

@admin.register(SignupData)
class SignupDataAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_email', 'get_password', 'phone_number', 'address', 'country', 'country_code']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_password(self, obj):
        return obj.user.password  
    get_password.short_description = 'Password'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'size', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'get_username', 'get_email', 'phone_number', 'address',
        'country', 'country_code', 'ordered_products',
        'total_price', 'delivery_charge', 'combined_total',
        'payment_method', 'transaction_id', 'status', 'created_at'
    ]
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['user__username', 'transaction_id', 'ordered_products']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'