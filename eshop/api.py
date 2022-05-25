from rest_framework.routers import DefaultRouter

# from account.api_views import LoginView
from order.api_views import OrderViewset, OrderDetailViewset,OrderCustomerViewSet
from product.api_views import ProductViewset, CategoryViewset, CartViewSet

router = DefaultRouter()
##Products
router.register('product',ProductViewset,basename='api_product')
router.register('category',CategoryViewset,basename='api_category')

#Orders
router.register('order',OrderViewset,basename='api_order')
router.register('order_detail',OrderDetailViewset,basename='api_order_detail')
router.register('cart',CartViewSet,basename='api_cart')
router.register('customer_orders',OrderCustomerViewSet,basename='customer_orders')

##AUTH
# router.register('login',LoginView,basename='login')
