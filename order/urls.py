from django.urls import path
from .views import *



urlpatterns = [
    path('',order,name='order'),
    path('in_card/',in_card,name='in_card'),
    path('edit/', product_quantity, name='order_edit'),
    path('add-cart/',add_cart,name='add_cart'),
    path('complete/',order_complete,name='order_complete'),
    path('continue/',order_continue,name='continue'),
    path('delete/<int:id>/',delete_order,name='delete_order'),
]
