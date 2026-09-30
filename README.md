# Diario Django - CRUD Completo

Aplicación Django que implementa un CRUD completo sobre el modelo `DiarioMiki` usando Class-Based Views (`ListView`, `DetailView`, `UpdateView`, `DeleteView`, `CreateView`), junto con un formulario de perfil de usuario.

## Requisitos previos

- Python 3.10 o superior
- pip
- Git (opcional, solo si clonas desde un repositorio)

## Instalación

1. **Clona el repositorio** (o descarga y descomprime el .zip):

   ```bash
   git clone https://github.com/fabiolamedrano/MedranoFabiola_CRUDDiarioDjango.git
   cd MedranoFabiola_CRUDDiarioDjango
   ```

2. **Crea un entorno virtual**:

   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual**:

   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Aplica las migraciones** para crear la base de datos:

   ```bash
   python manage.py migrate
   ```

6. **Crea un superusuario** para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser nombre_usuario
   ```

## Ejecución

Corra el servidor:

```bash
python manage.py runserver
```

Abra su navegador en:

```
http://127.0.0.1:8000/crear-perfil/
```

> **Nota:** la ruta raíz (`/`) no tiene una vista asignada en este proyecto, por lo que se debe entrar directamente a ` crear-perfil/` o a cualquiera de las rutas listadas abajo.

## Primer uso (importante)

Los formularios de perfil y de entrada de diario incluyen un campo "Usuario" que se llena con los usuarios existentes en la base de datos. Además, el listado de entradas solo muestra las del usuario que tiene la sesión iniciada. Por eso, antes de usar la aplicación por primera vez:

1. **Crea un superusuario** (esto también sirve como el primer usuario disponible en los formularios):

   ```bash
   python manage.py createsuperuser nombre_usuario
   ```

2. **Inicia sesión en `/admin/`** con esas credenciales:

   ```
   http://127.0.0.1:8000/admin/
   ```

   Esto autentica la sesión para todo el sitio, no solo para el panel de administración.

3. **Crea tu perfil** en `/crear-perfil/`, seleccionando tu usuario en el campo "Usuario". Al guardar, se te redirige automáticamente al listado de entradas (`/diario/lista/`).

4. **Desde el listado**, haz clic en "Nueva entrada" para crear la primera entrada de diario, seleccionando de nuevo tu usuario. Al guardar, vuelves al listado, donde ya verás la entrada creada.

## Rutas principales

| Acción                      | URL                              |
|------------------------------|-----------------------------------|
| Crear perfil de usuario       | `/crear-perfil/`                 |
| Crear entrada de diario       | `/crear-entrada/`                |
| Listar entradas del diario    | `/diario/lista/`                 |
| Ver detalle de una entrada    | `/diario/detalle/<int:pk>/`      |
| Editar una entrada            | `/diario/editar/<int:pk>/`       |
| Eliminar una entrada          | `/diario/eliminar/<int:pk>/`     |

## Notas

- Los estilos están hechos con Tailwind CSS (vía CDN) y la tipografía Poppins (vía Google Fonts), sin necesidad de instalar dependencias adicionales de frontend.
- El formulario usa `django-widget-tweaks` para aplicar clases de Tailwind a los campos generados por Django.