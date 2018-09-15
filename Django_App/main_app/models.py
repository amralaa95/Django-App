from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)