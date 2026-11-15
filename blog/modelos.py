class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }
    def __str__(self):
        return f"Nombre :{self.nombre} | Bio: {self.bio}"
class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo 
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado
    def to_dict(self):
        return {
            "id" : self.id,
            "titulo" : self.titulo,
            "contenido" : self.contenido,
            "autor" : self.autor.to_dict(),
            "tags" : self.tags,
            "estado" : self.estado
        }
    def __str__(self):
        return f"Id: {self.id} | Titulo: {self.titulo} | Autor: {self.autor.nombre}"
class Blog:
    def __init__(self):
        self.posts = []
    def buscar_por_titulo(self, titulo_buscado):
        resultados = []
        for p in self.posts:
            if titulo_buscado.lower() in p.titulo.lower():
                resultados.append(p.titulo)
        return resultados
    def listar_posts(self):
            if not self.posts:
                print("no hay posts para mostrar")
            else:
                for p in self.posts:
                    print(f"ID: {p.id} Titulo: {p.titulo}, Autor: {p.autor.nombre}")
    def filtrar_por_tags(self, tag_buscado):
        post_por_tag = []
        for p in self.posts:
            if any(tag_buscado.lower() in t.lower() for t in p.tags):
                post_por_tag.append(p)
        return post_por_tag
    def crear_post(self, titulo, contenido, autor, tags, estado):
        if self.posts:
            nuevo_id = max(p.id for p in self.posts)+1
        else:
            nuevo_id = 1
        nuevo_post = Post(nuevo_id, titulo, contenido, autor, tags, estado)
        self.posts.append(nuevo_post)
        return nuevo_post
    def convertir_lista(self):
        return [p.to_dict() for p in self.posts]
    def validar_post(self, post):
        if not post.titulo.strip():
            return False
        if not post.contenido.strip():
            return False
        if not post.autor.nombre.strip(): 
            return False
        return True
    def validar_todos(self):
        error_encontrado = False
        for post in self.posts:
            if not self.validar_post(post):
                print(f"el post: {post.id} no paso la validación (revisa titulo, contenido y autor)")
                error_encontrado = True
        if not error_encontrado:
            print("todos los posts pasaron la verificacion exitosamente")
    def obtener_posts(self):
        return self.posts
    
            

        
