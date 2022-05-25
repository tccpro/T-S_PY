def get_order_count(request):
    if request.user.is_authenticated:
        orders = request.user.orders.all()
        if orders:
            order = orders.order_by('-id').first()
            if  order.status == 'PENDING':
                return order.item_count()
    return 0

def get_orders(request):
    if request.user.is_authenticated:
        orders = request.user.orders.all()
        if orders:
            order = orders.order_by('-id').first()
            if order.status == 'PENDING':
                return order.details.all()
        else:
            return []
    return []