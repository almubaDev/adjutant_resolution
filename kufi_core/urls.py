from django.urls import path
from . import views

app_name = 'kufi_core'

urlpatterns = [
    path('', views.home_kufi, name='home_kufi'),
]
