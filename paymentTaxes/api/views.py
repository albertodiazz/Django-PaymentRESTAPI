from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import Boletas
import json


# Create your views here.
class PaymentServices(View):
    '''
    Esta clase sirve para comprobar los tickets pagados 
    o pendientes y pagarlos  
    '''

    def get(self, request, 
            statusPayment:str,
            servicesType:str):
        '''
        Obtenemos la informacion de nuestros servicios

        Args:
            [statusPayment] [str] : [filtramnos entre pending y paid]
            [servicesType] [str] : [filtramnos el servicio que queremos]
        '''

        if (statusPayment.lower() == 'pending' or statusPayment.lower() == 'paid'):
            boletas = list(Boletas.objects.filter(category= servicesType.lower(), 
                                                  statusPayment= statusPayment.lower()).values()) 
            if (len(boletas) == 0):
                result = 200
                body = 'No se encontraron boletas: {} {}'.format(statusPayment.lower(),
                                                                 servicesType.lower())
            else: 
                result = 200
                body = []
                # TODO : REFACT
                for i in range(len(boletas)):
                    body.append({'expirationDate': boletas[i]['expirationDate'],
                                 'cost': boletas[i]['cost'],
                                 'paymentReference': boletas[i]['barCode']})

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


class Transactions(View):
    '''
    Esta clase sirve para comprobar las trasacciones realizadas en periodos deseados
    '''

    def get(self, request):
        # Get importe acumulado osea todo el varo que nos ha entrado
        pass

    def post(self, request):
        # TODO : NOTA
        # Ocupamos Post por que debemos crear una nueva identidad
        # que modifique el status de nuetros servicios pero que genere
        # su propia base de datos
        pass
