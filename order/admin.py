from django.contrib import admin
from .models import Order,Order_detail
class OrderDetailAdmin(admin.ModelAdmin):
    list_display=['id','product','order','quantity']
    list_display_links = ['id','order']
admin.site.register(Order)
admin.site.register(Order_detail,OrderDetailAdmin)