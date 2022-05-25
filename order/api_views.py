from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from order.models import Order,Order_detail
from order.serializers import OrderSerializer,OrderDetailSerializer

class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewset(ModelViewSet):
    queryset = Order_detail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderCustomerViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,]
    def list(self, request, *args, **kwargs):
        user = request.user
        order_data = Order.objects.filter(customer=user)
        return Response({
            'orders':[
                {
                    'order_id':order.id,
                    'order_date':order.order_date,
                    'expired_date':order.expired_date,
                    'price':order.total_price(),
                    'item_count':order.item_count(),
                    'status':order.status
                }
                for order in order_data
            ]
        })