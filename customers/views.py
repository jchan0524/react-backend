from customers.models import customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer

def customers(request):
    #invoke serializer and return to client
    data = customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})

def Customer(request, id):
    try:
        data = customer.objects.get(pk=id)
    except customer.DoesNotExist: 
        raise Http404('Customer does not exist')
    
    serializer = CustomerSerializer(data)
    return JsonResponse({'customer': serializer.data})