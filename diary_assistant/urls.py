from django.urls import path
from . import views

app_name = 'diary_assistant'

urlpatterns = [
    path('', views.dashboard_diary, name='dashboard_diary'),
]