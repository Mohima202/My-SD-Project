from .models import CartItem

def cart_item_count(request):
    if request.user.is_authenticated:
        count = sum(item.quantity for item in CartItem.objects.filter(user=request.user))
    else:
        count = 0
    return {'total_items': count}




from .models import CartItem

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_items = sum(item.quantity for item in cart_items)
    else:
        total_items = 0
    return {
        'cart_item_count': total_items
    }