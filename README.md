# IoTFacebook
Generación de una publicación en Facebook mediante internet de las cosas (IoT internet of things), utilizando la plataforma IFTTT (If this then that).

Este programa esta escrito en Python, esta hecho utilizando los servicios de la plataforma ifttt.com 
Los componentes necesarios para crear este proyecto son:
- 1 Raspberry Pi.
- 1 memoria SD con el sistema operativo raspbian.
- 1 LDR (sensor de luz).
- 1 capacitor.
- 1 protoboard.
- 1 cable plano (ribbon cable).
- los cables necesarios para conectar, pin, corriente y tierra.
- internet.
- Pantalla, mouse y teclado (opcional). 
(se puede usar en modo VNC, con el cual puedes utilizar la raspberry como una maquina virtual en tu equipo. link de tutorial: http://www.frambuesapi.co/2013/10/07/conexion-remota-al-raspberry-pi-usando-vnc/ )

Se usan 2 applets de la página ifttt.com donde creamos una para el estado de día y otra para el estado de noche.

1.-Vamos a la opcion "My Applets"

2.-New Applet 

3.-Click en this, buscamos el servicio de Maker Webhooks.

4.-Creamos un web request dandole un nombre.

5.-Click en that, después buscamos Facebook > create a status message > aquí escribimos lo que queremos añadiendo un valor con "add ingredient" que es lo que queremos enviar en el programa en este caso enviaremos "día" o "noche" dependiendo del caso,creamos la acción, y repetimos lo mismo para el siguiente que falte (estado de día o de noche).

6.-Ya que tenemos creados nuestros applets, vamos a ifttt.com en la sección "search" buscamos "Maker  Webhooks", clic sobre el y despues clic en el boton connect, si este no les aparece, en la parte superior derecha, aparecera un botón con un engrane que dirá settings, damos clic en el y nos mandara a una pagina con cierta informacion, copiamos el link en el apartado de URL y lo pegamos en el browser.

7.-En esta página copiaremos el primer link que nos proporciona, el que tiene {event}, que es donde pondremos el nombre de nuestro applet.

8.-Vamos al programa y en la parte de 
"requests.post("Aquí tu link de IFTTT", data=report)" pegamos el link dentro de las comillas que contienen "Aquí tu link IFTTT".

9.- Ahora conectamos nuestra raspberry debidamente con sus componentes eh internet, corremos el programa, y listo :D
