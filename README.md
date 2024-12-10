# Administrador de Productos e Inventario

Este proyecto es una aplicación web para gestionar productos e inventario. Fue desarrollado utilizando **Django** y **Django REST Framework (DRF)**, con una separación clara entre el manejo de formularios y plantillas en Django, y la gestión de API REST con DRF.

## 🚀 Funcionalidades

### Productos
- **Crear:** Agregar nuevos productos con nombre, descripción, precio, imagen y cantidad inicial.
- **Visualizar:** Listar productos con opciones de búsqueda y filtrado.
- **Editar:** Modificar información existente de un producto.
- **Eliminar:** Eliminar productos del sistema.

### Movimientos de Inventario
- **Entradas y salidas:** Registrar movimientos de productos para ajustar la cantidad disponible.

### Autenticación
- **Inicio de sesión**: Sistema de autenticación mediante **JWT (JSON Web Tokens)**.

---

## 🛠️ Tecnologías Utilizadas
- **Version de Python**: 3.12.4
- **Backend**: Django 5.x, Django REST Framework.
- **Base de Datos**: PostgreSQL 16.
- **Frontend**: Formularios y plantillas gestionadas con Django.

---

## ⚙️ Configuración del Proyecto

## Metodo 1: Sin Docker

### 1️⃣ Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

### 2️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto y define las siguientes variables:
```env
NAME= ""
USER= ""
PASSWORD= ""
HOST= ""
PORT= ""
```
Las variables hacen referencia a los datos de conexion de la base de datos
### 4️⃣ Migrar la Base de Datos
```bash
python manage.py migrate
```

### 5️⃣ Crear un Superusuario
```bash
python manage.py createsuperuser
```

### 6️⃣ Iniciar el Servidor
```bash
python manage.py runserver
```
## 🐳 Método 2: Utilizando Docker y PostgreSQL

### 1️⃣ Ubicarse en la Carpeta Raíz del Proyecto
Asegúrate de estar en el directorio raíz del proyecto donde se encuentran los archivos `Dockerfile` y `docker-compose.yml`.

### 2️⃣ Configurar la Base de Datos Localmente con PostgreSQL
Se incluye un archivo llamado `script.sql` en la carpeta raíz del proyecto. Este archivo contiene las instrucciones SQL necesarias para inicializar la base de datos. Sigue estos pasos para configurarlo localmente:

1. Abre la terminal de PostgreSQL o utiliza una herramienta de administración como **pgAdmin**.
2. Crea una nueva base de datos:
   ```sql
   CREATE DATABASE nombre_base_datos;
   ```
3. Importa el archivo `script.sql` a la base de datos recién creada:
   - Desde la línea de comandos:
     ```bash
     psql -U <usuario> -d nombre_base_datos -f script.sql
     ```
   - O en **pgAdmin**, utiliza la opción "Query Tool" para ejecutar el contenido del archivo.

4. Verifica que la base de datos se haya configurado correctamente y contenga las tablas y datos iniciales.

### 3️⃣ Construir y Levantar los Contenedores
Una vez configurada la base de datos local, utiliza Docker para levantar la aplicación:

Ejecuta el siguiente comando para construir las imágenes y levantar los contenedores:
   ```bash
   docker-compose up --build
   ```

La aplicación estará disponible en:
   ```
   http://localhost:8000
   ```

### 4️⃣ Parar los Contenedores
Para detener los contenedores y limpiar recursos asociados, utiliza:
```bash
docker-compose down
```

---

## 🛠️ Notas

- **Configuración de Variables de Entorno:** En el archivo `.env` o `docker-compose.yml`, asegúrate de incluir las credenciales y la URL de conexión de tu base de datos PostgreSQL local.
- **Migraciones:** El archivo `script.sql` debe coincidir con las migraciones del proyecto Django para evitar conflictos. Si realizas cambios en los modelos, actualiza el archivo SQL en consecuencia.
- **Sincronización con Docker:** Aunque la base de datos se administra localmente, la aplicación en Docker debe conectarse a ella usando las credenciales correctas. Puedes utilizar host.docker.internal en la variable "HOST" para conectarte desde el contenedor a la base local
```bash
docker-compose up -d
```


---

## 🖥️ Uso de la API REST

La aplicación cuenta con un módulo independiente para gestionar las solicitudes API. Todas las peticiones deben ser autenticadas con un token JWT.

### 🔐 Autenticación

1. **Obtener un Token**
   Realiza una solicitud `POST` al endpoint `/api/token/` con el siguiente cuerpo:
   ```json
   {
       "username": "tu_usuario",
       "password": "tu_contraseña"
   }
   ```
   Esto devolverá un par de tokens (`access` y `refresh`).

2. **Usar el Token de Acceso**
   Agrega el token en la cabecera de tus solicitudes:
   ```http
   Authorization: Bearer <token_de_acceso>
   ```

### 📋 Endpoints Principales

#### Productos
- `GET /api/productos/` - Listar productos.
- `POST /api/productos/` - Crear un nuevo producto.
- `PUT /api/productos/<id>/` - Actualizar un producto.
- `DELETE /api/productos/<id>/` - Eliminar un producto.

#### Movimientos de Inventario
- `POST /api/movimientos/` - Registrar un movimiento de entrada o salida.
- `GET /api/movimiento/` - Lista de los movimientos.
---

## 🔧 Notas Adicionales

- La interfaz de usuario (formularios y plantillas) se gestiona con Django como un administrador de plantillas.
- Puedes utilizar herramientas como **Postman** para interactuar con la API REST.
- Asegúrate de estar autenticado para realizar solicitudes a los endpoints protegidos.
