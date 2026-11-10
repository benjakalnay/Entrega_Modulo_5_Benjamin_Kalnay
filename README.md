Proyecto: Blog por Consola
Descripcion general: Gestión y consulta de posts con menu interactivo
Arbol de carpetas: 
proyecto_blog/
│── main.py
│── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
1. la carpeta main.py es la principal donde se muestra el menu y se dervia a la funcion indicada de acuerdo a la opcion elegida por usuario
2. REDME.md es este mismo documento explicando el uso del blog
3. La carpeta blog contiene todos la informacion y funciones necesarias para el correcto funcionamiento
4. Esta carpeta le infroma a Python que es un paquete
5. La carpeta datos.py contiene los posts, los estados y toda la informacion pertinente para las funciones
6. Menu.py muestra el menu y le pide el input al usuario.
7. la carpeta operaciones.py contiene 3 funciones, una para listar todos los posts, otra para bsucar por titutlo y la tercera para filtrar por tags. Las ultimas dos estan preparadas para recibir culauqier input y no dar error de sistema.
8. por ultimo, validaciones.py hace un repaso post por post para corroborar que contenga todos los datos precisados. 
