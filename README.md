
# 📚 Biblioteca — Proyecto Django Visual 2025

Proyecto desarrollado en Django que permite a los usuarios:

- Subir libros en formato PDF.
- Visualizar listado de libros con detalles (autor, género, fecha).
- Calificar y comentar libros.
- Visualizar libros similares basados en género.
- Gestión de usuarios con login/logout.
- API REST para gestión de autores, géneros, libros y calificaciones con autenticación JWT.

---

## 🚀 Instalación Paso a Paso

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu_usuario/biblioteca.git
cd biblioteca
```

2. **Crear y activar entorno virtual:**

```bash
python -m venv env
env\Scripts\activate      # Windows CMD
source env/bin/activate   # Linux/macOS
```

3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

*Si no tenés `requirements.txt`, instalá manualmente:*

```bash
pip install django djangorestframework djangorestframework-simplejwt pandas
```

4. **Realizar migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (administrador):**

```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor local:**

```bash
python manage.py runserver
```

---

## 🖥️ Uso y Navegación Web

- **Inicio:**  
  `http://127.0.0.1:8000/` — Página principal con diseño moderno y botones para navegar.

- **Login:**  
  `http://127.0.0.1:8000/api/auth/login/` — Inicio de sesión para usuarios registrados.

- **Listado de libros:**  
  `http://127.0.0.1:8000/libros/listar/` — Ver todos los libros con detalles y opciones para calificar y descargar PDF.

- **Subir libro:**  
  `http://127.0.0.1:8000/libros/subir/` — Formulario para agregar nuevos libros (requiere login).

- **Calificar libro:**  
  Desde botón en listado, ejemplo:  
  `http://127.0.0.1:8000/libros/calificar/<id_libro>/`

- **Admin Django:**  
  `http://127.0.0.1:8000/admin/` — Panel para gestión avanzada (autores, géneros, libros, calificaciones).

---

## 🔗 API REST

Endpoints protegidos con JWT para administración y consumo desde Postman u otras aplicaciones:

| Método | Endpoint                      | Descripción                 |
|--------|-------------------------------|-----------------------------|
| GET    | `/api/autor/`                 | Listar autores              |
| POST   | `/api/autor/nuevo/`           | Crear autor                 |
| GET    | `/api/genero/`                | Listar géneros              |
| POST   | `/api/genero/nuevo/`          | Crear género                |
| GET    | `/api/libro/`                 | Listar libros               |
| POST   | `/api/libro/nuevo/`           | Crear libro                 |
| GET    | `/api/calificacion/`          | Listar calificaciones       |
| POST   | `/api/calificacion/nueva/`    | Crear calificación          |

---

## 📊 Script de Valoraciones y Gráficos

- Se usa **pandas** para analizar las calificaciones guardadas.
- Se generan gráficos para determinar:
  - Género más valorado.
  - Libro con mejor puntuación.
  - Distribución de valoraciones por autor y género.

*Los gráficos pueden visualizarse y exportarse usando Google Colab o Jupyter Notebooks.*

---

## 🎨 Diseño Visual

- Tema oscuro con degradados azules y verdes.
- Navbar fija y translúcida con efecto blur.
- Cards con bordes asimétricos y sombras intensas.
- Botones con efecto “glow” animado en hover.
- Tipografía moderna “Montserrat” de Google Fonts.
- Uso de íconos Bootstrap para mejor UX.

---

## 📂 Estructura del Proyecto

```
BIBLIOTECA/
├── biblioteca/            # Configuración Django principal (renombrada desde libroteka)
├── accounts/              # Módulo de autenticación y login
├── libros/                # Gestión principal: libros, autores, géneros, calificaciones
├── storage/               # Archivos PDF subidos
├── db.sqlite3             # Base de datos SQLite
└── manage.py
```

---

## 🧾 Dependencias

- Django==5.2.4
- djangorestframework==3.16.0
- djangorestframework-simplejwt==5.5.0
- pandas==2.x.x
- Bootstrap 5 (CDN en templates)

---

## 🔐 Licencias

- Python: PSF License  
- Django: BSD-3-Clause  
- Bootstrap: MIT  
- Pandas: BSD  
- Django REST Framework: BSD

---

## ✨ Créditos

- Proyecto desarrollado y estilizado en 2025 por el equipo de desarrollo.  
- Asistencia técnica con IA para diseño y desarrollo funcional.

---

**¡Gracias por usar Biblioteca!**
