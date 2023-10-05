from django.urls import path
from . import views

urlpatterns = [
    path('tareas', views.tareas, name='tareas'),
    path('testeo2/', views.initPerfil),
]