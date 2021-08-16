from django.db import models


# Create your models here.
class Contact(models.Model):
    first_Name = models.CharField(source="firstName", max_length=100)
    last_Name = models.CharField(source="lastName", max_length=100)
    phone_Number = models.CharField(source="phoneNumber", max_length=30)
    email = models.EmailField(source="lblEmail")
    message = models.CharField(source="lblMessage", max_length=1000)
    create_list = models.DateTimeField(auto_created=True)

    @classmethod
    def is_valid(cls):
        pass
