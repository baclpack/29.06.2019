from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

from blog.models import *

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    product = {
        models.OneToOneField(Product_TV, on_delete=models.SET_NULL, null=True, blank=True),
        models.OneToOneField(Product_Phone, on_delete=models.SET_NULL, null=True, blank=True),
        models.OneToOneField(Product_a_laptop, on_delete=models.SET_NULL, null=True, blank=True),
    }
    boolean = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return "{}".format(self.product.title)


class Cart(models.Model):
    cartitem = models.ManyToManyField(CartItem)
    decimal = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    
    def __str__(self):
        return str(self.id)