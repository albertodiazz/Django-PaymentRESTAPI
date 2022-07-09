from django.urls import path
from .views import PaymentServices


urlpatterns = [
    path('boletas/', PaymentServices.as_view(), name='get_boletas_all'),
    path('boletas/<str:statusPayment>/<str:servicesType>', PaymentServices.as_view(), name='get_boletas_statusPayment'),
]
