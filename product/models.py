from django.db import models
from order.models import *
from django_currentuser.middleware import get_current_authenticated_user
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name or 'nul'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    quantity = models.IntegerField(default=0)

    def get_status(self):
        if self.quantity>0:
            cuser = get_current_authenticated_user()
            if cuser:
                if cuser.orders.all():
                    order = cuser.orders.all().last()
                    for item in order.details.all():
                        if item.product == self:
                            return 'Added to cart'
                    return 'Add to cart'
                else:
                    return 'Add to cart'
            else:
                return 'Add to cart'
        else:
            return 'Unavailable'

    @property
    def get_url(self):
        if self.image:
            return self.image.url
        return '/static/images/default_shop.jpg'

    def __str__(self):
        return self.name or 'nul'