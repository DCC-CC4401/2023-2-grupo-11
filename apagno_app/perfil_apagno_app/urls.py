from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('crear_evento', views.creacionEvento, name='nuevo evento'), # link al formulario del evento
    path('testeo2/', views.initPerfil), # link a la pagina de perfil (por ahora testeo)
    path('register', views.register_user, name='register_user'), # link al formulario de registro
    path('login',views.login_user, name='login'), # link al formulario de inicio de sesion
    path('logout',views.logout_user, name='logout'), # link al formulario de cierre de sesion
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
