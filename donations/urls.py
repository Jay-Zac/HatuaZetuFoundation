from django.urls import path
from . import views

app_name = 'donations'  # Namespace for URLs

urlpatterns = [
    path('', views.create_payment, name='donate'),  # Handle payment creation
    path('payment-executed/', views.execute_payment, name='payment_executed'),  # Handle payment execution
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),  # Handle payment cancellation
    path('thank-you/', views.payment_executed, name='thank_you'),  # Thank you page
]
