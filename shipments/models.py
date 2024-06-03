from django.db import models
from product.models import Product
from user.models import CustomUser


class Shipments (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    approved = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
