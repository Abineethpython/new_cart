from django.db import models
from customers.models import Customer
from product.models import product
# Create your models here.
class order(models.Model):
    objects = models.Manager()
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    ORDER_CHOICES = ((ORDER_PROCESSED,'ORDER_PROCESSED'),
                     (ORDER_PROCESSED, 'ORDER_CONFIRMED'),
                     (ORDER_DELIVERED,'ORDER_DELIVERED'),
                     (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status = models.IntegerField(choices=ORDER_CHOICES,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "order-{}-{}".format(self.id,self.owner.name)

class ordereditem(models.Model):
    objects = models.Manager()
    product = models.ForeignKey(product,on_delete=models.SET_NULL,null=True,related_name='added_cart')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_items')





