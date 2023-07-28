from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class AddField(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, blank=True, null=True)


# class User(AbstractUser):
#     country = models.CharField(max_length=50,blank=True,null=True)
    






