from customers.models import customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer

def customers(request):
    #invoke serializer and return to client
    data = customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})