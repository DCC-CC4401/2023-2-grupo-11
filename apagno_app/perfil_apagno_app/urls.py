from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import MyProfile

from . import views

# Importamos las vistas de autenticacion de django
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('crear_evento', views.creacionEvento, name='nuevo evento'), # link al formulario del evento
    path('testeo2/', views.initPerfil), # link a la pagina de perfil (por ahora testeo)
    path('register', views.register_user, name='register_user'), # link al formulario de registro
    path('login',views.login_user, name='login'), # link al formulario de inicio de sesion
    path('logout',views.logout_user, name='logout'), # link al formulario de cierre de sesion
    path('password-reset/',  # link al formulario de reseteo de contraseña
        PasswordResetView.as_view(  # vista de django para resetear contraseña
            template_name='users/password_reset.html',
            html_email_template_name='users/password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'), # link a la pagina de confirmacion de reseteo de contraseña
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'), # link a la pagina de confirmacion de reseteo de contraseña
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'), # link a la pagina de confirmacion de reseteo de contraseña
    path('', views.Eventos.as_view(), name='perfil'), # link a la pagina de perfil
    path('evento/abandonar/<int:pk>', views.AbandonarEventoView.as_view(), name='abandonar_evento'), # link a la pagina de abandonar evento
    path('evento/<int:pk>', views.EventoDetail.as_view(), name='evento'), # link a la pagina de detalle de evento
    path('evento/editar/<int:pk>', views.EventoUpdate.as_view(), name='editar_evento'), # link a la pagina de editar evento
    path('evento/eliminar/<int:pk>/', views.EventoDelete.as_view(),name='eliminar_evento'), # link a la pagina de eliminar evento
    path('profile/', MyProfile.as_view(), name='profile'), # link a la pagina de perfil
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # para que se puedan ver las imagenes en el perfil
