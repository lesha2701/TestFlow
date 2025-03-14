from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autotest(models.Model):
    name = models.CharField(max_length=50)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

