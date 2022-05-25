from rest_framework.serializers import ModelSerializer

from order.models import Order, Order_detail


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = Order_detail
        fields = '__all__'