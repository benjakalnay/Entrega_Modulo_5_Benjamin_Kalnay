perfil_autor = {
"nombre": "Benjamin Kalnay",
"bio": "licenciado en marketing y estudiante de IA",    
"especialidad": "python",
"redes_sociales": ["@benjakalnay", "@whojuy"],
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"python", "django", "web", "backend", "python"}
posts = [
    {
        "id": 1,
        "titulo": "aprendiendo python",
        "contenido": "foto, comentarios",
        "autor": perfil_autor,
        "tags": ["python", "coderhouse"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "que es django",
        "contenido": "fotos, me gusta",
        "autor": perfil_autor,
        "tags": ["django", "blog"],
        "estado": "borrador",
    },
    {
        "id": 3,
        "titulo": "organizando datos con diccionarios",
        "contenido": "comentarios",
        "autor": perfil_autor,
        "tags": ["python", "diccionarios"],
        "estado": "archivado", 
    },
    {
        "id": 4,
        "titulo": "",
        "comentarios": "",
        "autor": perfil_autor,
        "tags": ["coderhouse", "blog"],
        "estado": "publicado",   
    }
]