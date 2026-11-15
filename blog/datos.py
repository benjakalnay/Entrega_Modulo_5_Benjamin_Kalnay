import json
from blog.modelos import Autor, Post
def cargar_post(ruta_archivo = "posts.json"):
    posts_cargados = []
    try:
        with open(ruta_archivo, "r", encoding= "utf-8") as archivo:
            datos_json = json.load(archivo)
            for d in datos_json:
                autor = Autor(d["autor"]["nombre"], d["autor"]["bio"])
                post = Post(d["id"], d["titulo"], d["contenido"], autor, d["tags"], d["estado"])
                posts_cargados.append(post)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return posts_cargados
def guardar_post(lista_posts, ruta_archivo = "posts.json"):
    lista_diccionarios = [post.to_dict() for post in lista_posts]
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)