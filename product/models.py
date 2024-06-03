from django.db import models
from user.models import CustomUser


class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    employee = models.ForeignKey(CustomUser,
                                 on_delete=models.SET_NULL, null=True)
