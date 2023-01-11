from rest_framework import serializers
from customers.models import customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = customer
        fields = '__all__'