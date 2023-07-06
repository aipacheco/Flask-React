# Plantilla de WebApp con React JS y API de Flask

Construye aplicaciones web utilizando React.js para el front-end y python/flask para tu API de backend.

- Integrado con Pipenv para la gestión de paquetes.
- Uso del archivo .env.
- Integración de SQLAlchemy para la abstracción de base de datos.

### Preparación del entorno:

1. Instala Docker:
    - [Docker para Windows](https://docs.docker.com/desktop/install/windows-install/)
2. Instala Node para el front-end: [Node.js](https://nodejs.org/en/download)
3. Instala Python para el back-end: [Python](https://www.python.org/downloads/)

### Levantar el entorno:

1. Ejecuta `$ docker-compose up` para levantar la base de datos
2. Ejecuta en un terminal `$ docker-compose exec -it postgres /bin/bash`
3. Entra en la base de datos: `$ psql`
4. Crea la base de datos example `$ create database example;`
5. Comprueba que existe con `$ \l`
6. Ejecuta `$ pipenv shell`
7. A continuación instala los paquetes de python: `$ pipenv install`
8. Después, `$ npm install`
9. Antes de levantar el entorno, copia del .env.example las variables de entorno del DATABASE_URL y el BACKEND_URL.
10. Si hace falta ejecutar:
    - `$ pipenv run init` -> si no existe carpeta de migraciones
    - `$ pipenv run migrate`
    - `$ pipenv run upgrade`
11. A continuación, ejecuta:
    - `$ pipenv run start`
    - `$ npm run start`

## ¡Publica tu sitio web!

Esta plantilla está 100% lista para desplegarse con Render.com en cuestión de minutos.
