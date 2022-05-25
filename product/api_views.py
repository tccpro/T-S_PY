from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from utils.paginator import StandardResultsSetPagination
from .paginations import ProductPagination
from order.models import Order_detail
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        category = request.GET.get('category',None)
        queryset = self.get_queryset()
        if category:
            queryset = queryset.filter(category=category)
        page = self.paginate_queryset(queryset)
        if page is not None:
            data = []
            for obj in page:
                data.append(
                    {
                        "id": obj.id,
                        "name": obj.name,
                        "price": obj.price,
                        "image": "http://127.0.0.1:8000"+obj.get_url,
                        "quantity": obj.quantity,
                        "category": obj.category.id
                    }
                )
            return Response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 335077373
# 977850172
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, store_pk=None, locker_pk=None):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        category=Category.objects.create(
            name=request.data.get('name',None),
            description=request.data.get('description',None),
        )
        return Response(data={'status':'created'},status=HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs.get('pk'))
        category.name=request.data.get('name',None)
        category.description=request.data.get('description',None)
        category.save()

        return Response(status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        category=Category.objects.get(pk=kwargs.get('pk',None))
        category.delete()
        return Response(data={'status':'deleted'},status=HTTP_204_NO_CONTENT)

class CartViewSet(ModelViewSet):
    queryset = Order_detail.objects.all()
    permission_classes = [IsAuthenticated,]
    def list(self,request,*args,**kwargs):
        user = request.user
        order_details = Order_detail.objects.filter(order__customer=user)
        return Response({'items':[
            {
                'item_id':item.id,
                'order_id':item.order.id,
                'product':item.product.name,
                'quantity':item.quantity,
                'price':item.total_price()
            }
            for item in order_details
        ]})
