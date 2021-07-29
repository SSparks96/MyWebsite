from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
