from django.urls import path
from . import views

urlpatterns = [
    path('crear_evento', views.creacionEvento, name='nuevo evento'),
    path('testeo2/', views.initPerfil),
]