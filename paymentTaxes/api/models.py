from django.db import models
from datetime import timedelta, datetime
from .utils import create_bar_code 

# Create your models here.
class Boletas(models.Model):
    # TODO : NOTAS
    # Estas boletas solo pueden ser creadas por un super user
    # ---------------------------------------------------------
    # Tipo de servicio
    category = models.CharField(max_length=50)
    # Descripcion
    description = models.CharField(max_length=100) 
    # Fechas de vencimiento de un mes
    expirationDate = models.DateField(default=datetime.utcnow() + timedelta(weeks=4))
    # Importe del servicio
    cost = models.PositiveIntegerField()
    # Status de pago Pending, paid, etc
    statusPayment = models.CharField(max_length=50, 
                                     blank=True,
                                     editable=False,
                                     default='pending') 
    # Codigo de barras
    barCode = models.CharField(max_length=16, 
                               blank=True, 
                               editable=False,
                               default=create_bar_code)

    def save(self, *args, **kwargs):
        self.category = self.category.lower()
        self.statusPayment = self.statusPayment.lower()
        return super().save(*args, **kwargs)


class Cliente(models.Model):
    # Para saber la referencia que pago
    reference = models.CharField(max_length=16)
    paymentMethod = models.CharField(max_length=16)
    # Importe para abonar
    payment = models.PositiveIntegerField()
    # Para saber cuando pago
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Transactions(models.Model):
    # Con esto podemos ver las transacciones y apartir de ello
    # generar un algoritmo que visualize los adeudos y abonos
    category = models.CharField(max_length=50)
    amout = models.PositiveIntegerField(max_length=16) 
    reference = models.CharField(max_length=16) 
    statusPayment = models.CharField(max_length=50) 
    date = models.DateTimeField(auto_now_add=True, blank=True)

