"""apagno_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from apagno_app.views import index, destacados_logged
from django.conf import settings
from django.conf.urls.static import static
=======
from apagno_app.views import index, destacados_logged, destacados
>>>>>>> 8433d6ba7485235a26698954b5f97b666e8cb32f

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testeo/', index),
    path('perfil_apagno_app/', include('perfil_apagno_app.urls')),
    path('eventos-destacados-logged/', destacados_logged),
    path('eventos-destacados/', destacados),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
