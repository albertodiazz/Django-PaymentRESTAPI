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
    # TODO : PENDIENTE
    # [] Siempre que se creen deben ser pendientes
    statusPayment = models.CharField(max_length=50) 
    # Codigo de barras
    barCode = models.CharField(max_length=16, 
                               blank=True, 
                               editable=False,
                               default=create_bar_code)

    def save(self, *args, **kwargs):
        self.category = self.category.lower()
        self.statusPayment = self.statusPayment.lower()
        return super().save(*args, **kwargs)

