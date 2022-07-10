from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import datetime
from .utils import create_bar_code 
from .models import Boletas, Cliente, Transactions 
import json

# =================================
# TODO : SHAME 
# [] Me falto mostrar el formulario de tarjeta4 de debito o credito cuando
# estas son seleccionadas
# [] Me falto setear los rangos de fechas del pago del punto4
# =================================

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
        print(statusPayment.lower())
        if (statusPayment.lower() == 'pending' or statusPayment.lower() == 'paid' ):
            if statusPayment.lower() == 'pending':
                boletas = list(Boletas.objects.filter(category= servicesType.lower(), 
                                                      statusPayment= statusPayment.lower()).values()) 
            elif statusPayment.lower() == 'paid':
                boletas = list(Transactions.objects.filter(category= servicesType.lower(),
                                                           statusPayment= statusPayment.lower()).values()) 
            if (len(boletas) == 0):
                result = 200
                body = 'No se encontraron boletas: {} {}'.format(statusPayment.lower(),
                                                                 servicesType.lower())
            else: 
                result = 200
                body = []
                # TODO : REFACT
                acumulado, totalTransaciones = [], []
                for i in range(len(boletas)):
                    if statusPayment.lower() == 'paid':
                        acumulado.append(boletas[i]['amout'])
                        totalTransaciones.append(boletas[i]['reference'])
                        # body.append({'date': boletas[i]['date'],
                        #              'amout': boletas[i]['amout'],
                        #              'paymentReference': boletas[i]['reference']})
                    elif statusPayment.lower() == 'pending':
                        body.append({'expirationDate': boletas[i]['expirationDate'],
                                     'cost': boletas[i]['cost'],
                                     'paymentReference': boletas[i]['barCode']})
                if len(acumulado) > 0 and len(totalTransaciones) > 0:
                    body.append({'amout': sum(acumulado),
                                 'totalTransaciones': len(totalTransaciones)})

        else: 
            result = 400
            body = 'Malformed Request is pending or paid'
        datos = {
            'result': result,
            'body': body 
        }
        res = json.dumps(datos, cls= DjangoJSONEncoder)  
        return HttpResponse(res, content_type='application/json')


@csrf_exempt
def postform(request):
    # TODO : REFACT 
    response = """
        <form id='post-form' method='POST' actions='create'> 
        <label for="paymentMethod">Choose method payment:</label>
        <select id="paymentMethod" name="paymentMethod">
        <option value="debit_card">Debit Card</option>
        <option value="credit_card">Credit Card</option>
        <option value="cash">Cash</option>
        </select> 
        <p>Reference:</p>
        <input type='int' id='reference' name='reference'><br>
        <p>Mount:</p>
        <input type='text' id='payment' name='payment'><br>
        <input type='submit'>
        </form>
    """
    payment = request.POST.get('payment')
    reference = request.POST.get('reference')
    paymentMethod = request.POST.get('paymentMethod')
    if payment != None and reference != None:
        boletas = list(Boletas.objects.filter(barCode = int(reference)).values())
        print(boletas)
        if len(boletas) != 0 and boletas[0]['statusPayment'] == 'pending':
            print('La boleta con referencia: {} Existe'.format(reference))
            post= Cliente(payment=payment, reference=reference, paymentMethod=paymentMethod) 
            postT= Transactions(category=boletas[0]['category'], 
                                statusPayment='paid', 
                                amout=payment, 
                                reference=reference) 
            post.save()
            postT.save()
            response = """
                <p>Tu pago fue realizado con exito</p>
            """
        else:
            response = """
                <p>La referencia no Existe</p>
            """
            print('La boleta con referencia: {} No existe'.format(reference))
    return HttpResponse(response)
