from django.db import models

# Create your models here.
class Autotest(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)