from rest_framework import serializers
from .models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        field = {'id', 'firstname', 'lastname', 'phone', 'email', 'message'}

