# README
# 2023-2-grupo-11
Este proyecto "Apaño" consiste en una página web de eventos desarrollada en Django, que los usuarios planificar, organizar, gestionar y apuntarse a eventos propuestos por el resto de la comunidad. A continuación, se describen las principales características y funcionalidades de la aplicación.

## Funcionalidades principales

1. Crear un usuario y logearse

El ususario puede crear una cuenta por medio de la página de registro y logearse por medio de la pagina de login.

2. Acceso al perfil de usuario

Después de iniciar sesión, los usuarios pueden acceder a su perfil personal, donde se muestran los eventos creados y los eventos en los que participan.

3. Edición de perfil

En la página de perfil, los usuarios pueden editar su información, incluyendo nombre, correo, imagen de perfil y otros.

4. Formulario "Olvidaste tu contraseña"

Se proporciona un formulario para restablecer la contraseña en caso de olvido, enviando un correo con instrucciones para el cambio.

5. Creación de un evento

Usando una cuenta válida, se pueden crear eventos, rellenando un formulario con la información pertinente de este.

6. Enlistarse a eventos

Los usuarios pueden acceder al botón "Apaño" para enlistarse en los eventos de su interés.

7. Abandonar evento

Desde su perfil, los usuarios pueden cancelar su asistencia a un evento mediante el botón "Abandonar".

8. Cancelar evento

Los usuarios pueden cancelar la realización de un evento que han creado desde su perfil mediante el botón "Eliminar".

9. Creación y edición de eventos desde el perfil

Los usuarios pueden crear y editar eventos directamente desde la página de destacados y desde su perfil, sin ser redirigidos a otra página.

10. Navegación por la página de eventos

Se permite la navegación fácil entre los distintos tablones que muestran los eventos, facilitando la exploración de planes.

11. Ordenar eventos

Los eventos destacados en la página pueden ordenarse por fecha de celebración, ya sea de forma ascendente o descendente.

12. Filtrar eventos

Los eventos pueden filtrarse según diversas características, como tipo de evento, fecha, hora y estado (terminado o no terminado).

13. Acceder a información detallada del evento

Al hacer clic sobre la imagen de un evento, se despliega una ventana emergente con información adicional, incluyendo el creador y una descripción detallada.

14. Detalles del evento en el perfil

Los usuarios pueden ver detalles del evento al que planean asistir desde su perfil, presionando el botón "Ver".

## Requisitos de instalación
Para ejecutar la aplicación, se deben tener instalado Pytghon, Django y las librerias indicadas en el archivo *requirements.txt*.

## Configuración
Para correr la aplicación, se debe invocar el siguiente comando desde la carpeta *apagno_app*:
```
python manage.py runserver
```

Se iniciará la aplicacion en la dirección *http://localhost:8000/*, la cual de momento no esta seteada como pagina principal. A continuacion se muestran los links operativos:
- *http://localhost:8000/eventos_destacados-logged/* Página principal, donde se muestran los eventos.
- *http://localhost:8000/perfil_apagno_app/crear_evento* Formulario de creación de evento.
- *http://localhost:8000/perfil_apagno_app/register* Formulario de registro en la aplicación.
- *http://localhost:8000/perfil_apagno_app/login* Formulario de inicio de sesión.


