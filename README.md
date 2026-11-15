# Blog por Consola

Aplicación de consola en Python para crear, gestionar y consultar posts de un blog
mediante un menú interactivo. Los posts se guardan en un archivo JSON.

## Requisitos

- Python 3.x
- No requiere librerías externas (usa el módulo estándar `json`).

## Cómo ejecutarlo

Desde la carpeta raíz del proyecto (`proyecto_blog/`):

```bash
python main.py
```

> En macOS o Linux puede ser necesario usar `python3 main.py`.

## Estructura del proyecto

```
proyecto_blog/
├── main.py
├── README.md
├── posts.json
└── blog/
    ├── __init__.py
    ├── menu.py
    ├── modelos.py
    └── datos.py
```

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada. Carga los datos, muestra el menú y ejecuta la opción elegida. |
| `posts.json` | Archivo donde se almacenan los posts. |
| `blog/__init__.py` | Le indica a Python que `blog` es un paquete. |
| `blog/menu.py` | Muestra el menú y pide la opción al usuario. |
| `blog/modelos.py` | Contiene las clases `Autor`, `Post` y `Blog`. |
| `blog/datos.py` | Carga los posts desde `posts.json` y guarda los cambios en el archivo. |

## Arquitectura

El programa está organizado en tres clases, definidas en `modelos.py`.

### `Autor`

Representa al autor de un post. Atributos: ´nombre´ y ´bio´

### `Post`

Representa una publicación. Contiene sus datos y un objeto `Autor`.
Atributos: ´id´, ´título´, ´contenido´, autor, ´tags´ y ´estado´

`Autor` y `Post` incluyen los métodos:

- `to_dict()`: convierte el objeto en un diccionario para guardarlo en JSON.
- `__str__()`: define cómo se muestra el objeto al imprimirlo en consola.

### `Blog`

Administra la colección de posts. Métodos principales:

**Consulta**

- `listar_posts()`: muestra en consola el título y el autor de todos los posts.
- `buscar_por_titulo()`: busca los posts cuyo título coincide con el texto ingresado por el usuario.
- `filtrar_por_tags()`: busca los posts que contienen el tag ingresado y muestra sus títulos.
- `obtener_posts()`: devuelve la lista de todos los posts, tanto los cargados desde el archivo como los nuevos.

**Creación**

- `crear_post()`: crea un nuevo post a partir de los datos ingresados por consola.

**Validación**

- `validar_post()`: verifica que un post tenga todos los datos requeridos.
- `validar_todos()`: valida todos los posts y muestra en consola cuáles no pasaron la validación.

**Datos**

- `convertir_lista()`: convierte la lista de posts en una lista de diccionarios para guardarla en JSON.

## Persistencia de datos

Al iniciar, el programa carga los posts desde `posts.json` mediante `datos.py`.
Los posts nuevos se guardan en el archivo solo al elegir la opción **6. Guardar cambios y salir**.

> **Importante:** si se cierra el programa de otra forma, los cambios no guardados se pierden.

## Funcionalidades

1. **Listar posts**: muestra todos los posts disponibles.
2. **Buscar por título**: encuentra posts según su título.
3. **Filtrar por tags**: muestra los posts que tienen un tag determinado.
4. **Crear nuevo post**: permite cargar un post desde la consola.
5. **Validar posts**: revisa que todos los posts tengan sus datos completos.
6. **Guardar cambios y salir**: guarda los posts en `posts.json` y cierra el programa.

## Autor

Benjamín Kalnay
