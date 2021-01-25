# Python Web

## Django REST

### Episodio 2: Primeros *endpoints* y prueba usando un cliente de API-REST.

En este capítulo veremos cómo crear los primeros puntos de acceso (o *endpoints*) con los que podemos conectar un cliente sencillo como Postman o Insomnia y probarlo contra el servidor de Django-REST.

### Instalación de un cliente de API-REST

Dos ejemplos de clientes para probar APIs son: Postman e Insomnia. Puedes seguir los pasos de instalación en sus sitios web:

- [Postman](https://www.postman.com/downloads/)
- [Insomnia](https://support.insomnia.rest/article/23-installation)

En este y posteriores capítulos usaremos estos clientes para probar cada uno de los puntos de acceso que vayamos creando.

### Creación de nuestro primer punto de acceso.

Vamos a crear un punto de acceso (o *endpoint*) sencillo. Únicamente que nos retorne la respueta en formato JSON con un mensaje simple.

Pero, ¿dónde creamos este elemento?, la creación de una aplicación de Django instala muchos programas y con una estructura que a priori puede parecer confusa pero veremos que es bastante intuitiva.

Si te has fijado en el capítulo anterior, lanzamos el comando `startproject` y `startapp`. El entorno Django crea esta división por si tu proyecto tiene más de una aplicación (no será, en principio, nuestro caso).