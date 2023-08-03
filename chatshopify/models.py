from django.db import models
from django.contrib.auth.models import User


class AddField(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, blank=True, null=True)

    
    def __str__(self):
        return self.country
    
class UploadFile(models.Model):
    title =  models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='assets/')
    
    def __str__(self):
        return self.title