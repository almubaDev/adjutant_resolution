from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    path('users/', include('users.urls', namespace='users')),
    path('kufi/', include('kufi_core.urls', namespace='kufi_core')),
    path('diary/', include('diary_assistant.urls', namespace='diary_assistant')),
    path('soporte_tecnico/', include('tecnical_support.urls', namespace='soporte_tecnico')),
]
