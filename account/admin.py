from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number','first_name','last_name','username']
    list_display_links =['phone_number']
admin.site.register(User,UserAdmin)