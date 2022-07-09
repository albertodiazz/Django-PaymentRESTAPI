from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import Boletas
import json


# Create your views here.
class PaymentServices(View):

    def get(self, request, 
            statusPayment:str,
            servicesType:str):

        if (statusPayment.lower() == 'pending' or statusPayment.lower() == 'paid'):
            boletas = list(Boletas.objects.filter(category= servicesType.lower(), 
                                                  statusPayment= statusPayment.lower()).values()) 
            if (len(boletas) == 0):
                result = 200
                body = 'No se encontraron boletas: {}'.format(statusPayment.lower())
            else: 
                result = 200
                body = {'servicesType': boletas[0]['category'],
                        'expirationDate': boletas[0]['expirationDate'],
                        'cost': boletas[0]['cost'],
                        'paymentReference': boletas[0]['barCode']}

        else: 
            result = 400
            body = 'Malformed Request is pending or paid'
        datos = {
            'result': result,
            'body': body 
        }
        res = json.dumps(datos, cls= DjangoJSONEncoder)  
        return HttpResponse(res, content_type='application/json')

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
