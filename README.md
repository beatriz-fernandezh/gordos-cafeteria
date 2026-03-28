# Gordos Cafetería ☕

E-commerce desarrollado en Django como proyecto final de portafolio.

## Repositorio

[https://github.com/beatriz-fernandezh/gordos_cafeteria](https://github.com/beatriz-fernandezh/gordos_cafeteria)

---

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/gordos_cafeteria.git
cd gordos_cafeteria

# 2. Crea y activa el entorno virtual
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Instala las dependencias
pip install django
```

## Ejecutar en local

```bash
# Aplica las migraciones
python manage.py migrate

# Inicia el servidor
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en tu navegador.

---

## Rutas principales

| Ruta | Descripción | Acceso |
|------|-------------|--------|
| `/` | Catálogo de productos | Público |
| `/login/` | Iniciar sesión | Público |
| `/logout/` | Cerrar sesión | Autenticado |
| `/cart/` | Ver carrito | Público |
| `/checkout/` | Confirmar compra | Cliente autenticado |
| `/products/create/` | Crear producto | Solo admin |
| `/products/edit/<id>/` | Editar producto | Solo admin |
| `/products/delete/<id>/` | Eliminar producto | Solo admin |
| `/admin/` | Panel de administración Django | Solo admin |

---

## Credenciales de prueba

| Rol | Usuario | Contraseña |
|-----|---------|------------|
| Administrador | host | admin123 |
| Cliente | cliente | cliente1234 |

---

## Autora

Beatriz Fernández
