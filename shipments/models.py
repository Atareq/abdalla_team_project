from django.db import models
from product.models import Product
from user.models import CustomUser


class Shipments (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                 related_name='employee_shipments')
    approved = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    quentity = models.IntegerField(default=1)
    admin_approved = models.ForeignKey(CustomUser, null=True,
                                       on_delete=models.CASCADE,
                                       related_name='admin_shipments')
