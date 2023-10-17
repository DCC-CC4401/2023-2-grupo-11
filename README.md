# 2023-2-grupo-11
"Apaño" es una aplicación web creada utilizando Django, la cual permite al usuario planificar, organizar y gestionar eventos y permite a las personas unirse a estos eventos, sea con previo acuerdo o simplemente las ganas de asistir.

Actualmente, la aplicación permite al usuario crear una cuenta por medio de la página de registro y logearse por medio de la pagina de login. Usando dicha cuenta se puede crear eventos, los cuales se muestran en la pagina principal 
a medida que se van agregando. Los eventos contienen un nombre, host (normalmente el usuario que lo crea), categoria (las cuales se deben definir), fecha, hora, lugar, descripcion, y tambien esta la posibilidad de adjuntar una imagen 
relacionada al evento creado.

Es posible visualizar el listado de eventos disponibles desde la pagina principal (AKA eventos_destacados), donde se muestra en cajones el nombre del evento, la foto relacionada y la fecha de ocurrencia del mismo. Tambien hay un botón 
de "ver más", pero todavia no ha sido implementada la pagina de un evento especifico finalizado el sprint 1. Tambien existen dos botones, uno para acceder a la creación del evento en sí, o otro para ver mas eventos. El primero redirige 
al formulario de creación de evento, mientras que el segundo se encuentra bloqueado por el momento

Para cerrar la sesion, es posible apretar el boton "Cerrar sesión"

Para correr la aplicación, se deben tener instaladas las librerias indicadas en el archivo *requirements.txt*, y luego acceder a la carpeta *apagno_app*, desde la cual debe invocarse el comando
```
python manage.py runserver
```

Se iniciará la aplicacion en la dirección *http://localhost:8000/*, la cual de momento no esta seteada como pagina principal. A continuacion se muestran los links operativos:
- *http://localhost:8000/eventos_destacados/* Página principal, donde se muestran los eventos.
- *http://localhost:8000/perfil_apagno_app/crear_evento* Formulario de creación de evento.
- *http://localhost:8000/perfil_apagno_app/register* Formulario de registro en la aplicación.
- *http://localhost:8000/perfil_apagno_app/login* Formulario de inicio de sesión.

Las páginas de registro y login redirigen momentaneamente a una página en blanco, la cual se tiene proyectado a futuro que será la página del perfil de usuario. De momento la página principal funciona de nexo a las demás.
