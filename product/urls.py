from django.urls import path
from .views import home,product_detail,store
urlpatterns = [
    path('',home,name='home'),
    path('store/',store,name='store'),
    path('product_detail/<int:id>',product_detail,name='product_detail')
]
