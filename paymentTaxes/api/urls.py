from django.urls import path
from .views import PaymentServices, Transactions


urlpatterns = [
    path('boletas/', PaymentServices.as_view(), name='get_boletas_all'),
    path('boletas/<str:statusPayment>/<str:servicesType>', PaymentServices.as_view(), name='get_boletas_statusPayment'),
    path('transactions/', Transactions.as_view(), name='get_info'),
    path('transactions/<int:reference>/pay', Transactions.as_view(), name='post_pay'),
]
