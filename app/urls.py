from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('assistant/', views.assistant_view, name='assistant'),
]