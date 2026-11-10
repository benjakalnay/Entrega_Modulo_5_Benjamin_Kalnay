from .datos import estados_post
def validar_post(post):
    if type(post) is not dict:
        print(f"el post id: {post['id']} no es un diccionario")
        return False
    keys_obligatorias = {"id", "titulo", "autor", "contenido", "tags", "estado"}
    for keys in keys_obligatorias:
        if keys not in post:
            print(f"al post id: {post['id']} le falta la clave: {keys}")
            return False
    titulo = post.get("titulo","")
    if type(titulo) is not str:
        print(f"el titulo del posts id: {post['id']} no es correcto")
        return False
    elif len(titulo.strip()) == 0:
      print(f"no existe titulo del post id: {post['id']}")
      return False
    contenido = post.get("contenido","")
    if type(contenido) not in (str, int, float):
       print(f"contenido vacio del post id: {post['id']}")
       return False
    if type(contenido) is str and len(contenido.strip()) == 0:
        print(f"el post id: {post['id']} carece de contenido")
        return False
    autor = post.get("autor")
    if type(autor) is not dict:
        print(f"la llave autor del post id: {post['id']} no contiene un diccionario")
        return False
    if "nombre" not in autor:
        print(f"no existe la clave nombre dentro del diccionario del post id: {post['id']}")
        return False
    tags = post.get("tags")
    if type(tags) is not list:
        print(f"dentro del post id: {post['id']} no existe lista dentro de los tags")   
        return False   
    estados1 = post.get("estado")
    if estados1 not in estados_post:
        print(f"estado del post id: {post['id']} no identificado o vacio")
        return False
    return True