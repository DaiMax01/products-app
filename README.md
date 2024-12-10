
Administrador de Productos e Inventario
Este proyecto es una aplicación web para gestionar productos e inventario. Fue desarrollado utilizando Django y Django REST Framework (DRF), con una separación clara entre el manejo de formularios y plantillas en Django, y la gestión de API REST con DRF.

🚀 Funcionalidades
Productos
Crear: Agregar nuevos productos con nombre, descripción, precio, imagen y cantidad inicial.
Visualizar: Listar productos con opciones de búsqueda y filtrado.
Editar: Modificar información existente de un producto.
Eliminar: Eliminar productos del sistema.
Movimientos de Inventario
Entradas y salidas: Registrar movimientos de productos para ajustar la cantidad disponible.
Autenticación
Inicio de sesión: Sistema de autenticación mediante JWT (JSON Web Tokens).
🛠️ Tecnologías Utilizadas
Backend: Django 4.x, Django REST Framework.
Base de Datos: Base de datos relacional compatible con Django ORM.
Frontend: Formularios y plantillas gestionadas con Django.
⚙️ Configuración del Proyecto
1️⃣ Clonar el Repositorio
bash
Copiar código
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
2️⃣ Instalar Dependencias
bash
Copiar código
pip install -r requirements.txt
3️⃣ Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto y define las siguientes variables:

env
Copiar código
NAME= ""
USER= ""
PASSWORD= ""
HOST= "host.docker.internal"
PORT= "5432"
4️⃣ Migrar la Base de Datos
bash
Copiar código
python manage.py migrate
5️⃣ Crear un Superusuario
bash
Copiar código
python manage.py createsuperuser
6️⃣ Iniciar el Servidor
bash
Copiar código
python manage.py runserver
🖥️ Uso de la API REST
La aplicación cuenta con un módulo independiente para gestionar las solicitudes API. Todas las peticiones deben ser autenticadas con un token JWT.

🔐 Autenticación
Obtener un Token Realiza una solicitud POST al endpoint /api/token/ con el siguiente cuerpo:

json
Copiar código
{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}
Esto devolverá un par de tokens (access y refresh).

Usar el Token de Acceso Agrega el token en la cabecera de tus solicitudes:

http
Copiar código
Authorization: Bearer <token_de_acceso>
📋 Endpoints Principales
Productos
GET /api/productos/ - Listar productos.
POST /api/productos/ - Crear un nuevo producto.
PUT /api/productos/<id>/ - Actualizar un producto.
DELETE /api/productos/<id>/ - Eliminar un producto.
Movimientos de Inventario
POST /api/movimientos/ - Registrar un movimiento de entrada o salida.
🔧 Notas Adicionales
La interfaz de usuario (formularios y plantillas) se gestiona con Django como un administrador de plantillas.
Puedes utilizar herramientas como Postman para interactuar con la API REST.
Asegúrate de estar autenticado para realizar solicitudes a los endpoints protegidos.
📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

🌟 ¡Gracias por Usar Este Proyecto! 😊
