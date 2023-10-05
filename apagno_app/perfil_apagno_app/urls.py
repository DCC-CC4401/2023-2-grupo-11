from django.urls import path
from . import views

urlpatterns = [
    path('testeo2', views.initPerfil),
    path('register', views.register_user, name='register_user'),
    path('login',views.login_user, name='login'), 
]