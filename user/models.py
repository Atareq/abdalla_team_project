from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    userimage = models.ImageField(upload_to='user_images/')
    phonenumber = models.CharField(max_length=15,)
    is_admin = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=50)
