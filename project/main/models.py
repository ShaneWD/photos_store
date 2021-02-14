from django.db import models
from users.models import User
# Create your models here.
class Pictures(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pictures")
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    tags = models.CharField(max_length=100, default='')