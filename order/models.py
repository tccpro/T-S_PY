from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    STATUSES = [
        ('PENDING','pending'),
        ('INPROGRESS','inprogress'),
        ('COMPLETED','completed'),
        ('CANCELED','canceled')
    ]
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders',
        blank=True
    )
    order_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(null=True,blank=True)
    required_date = models.DateTimeField(null=True,blank=True)
    shipped_date = models.DateTimeField(null=True,blank=True)
    canceled_date = models.DateTimeField(null=True,blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default='PENDING'
    )
    def item_count(self):
        return self.details.count()
    def products(self):
        return self.details.all()
    def total_price(self):
        return sum([i.total_price() for i in self.details.all()])
    def __str__(self):
        return self.customer.__str__()+f'  order {self.id}' or 'nul'
class Order_detail(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name='details',
        null=True,
        blank=True

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders',
        blank=True
    )
    quantity = models.IntegerField(default=1)
    def total_price(self):
        return self.product.price*self.quantity

    def change_quantity(self,action,value=None):
        if action=='plus':
            if self.product.quantity>self.quantity:
                self.quantity+=1
        elif action == 'minus':
            if self.quantity>1:
                self.quantity-=1
        elif value:
            if value>self.product.quantity:
                value = self.product.quantity
            elif value<1:
                value = 1
            self.quantity = value
        self.save()
    def __str__(self):
        return str(self.id) or 'nul'
