from django.urls import path
from . import views

app_name = 'soporte_tecnico'

urlpatterns = [
    path('diagrama_kufi/', views.diagrama_kufi_view, name='diagrama_kufi'),
]
