def listar_posts(lista_posts):
    print("Posts:")
    for post in lista_posts:
        print(f"Titulo: {post['titulo']}, Autor: {post['autor']['nombre']}, Estado: {post['estado']}")

def buscar_por_titulo(lista, titulo):
    titulo_normalizado = titulo.strip().lower()
    encontrado = False
    for post in lista:
        if titulo_normalizado in post['titulo'].lower():
            print("-" * 24)
            print(f"Titulo: {post['titulo']}")
            print(f"Autor: {post['autor']['nombre']}")
            encontrado = True
            return 
    if not encontrado:
        print("no se encontraron coincidencias")

def filtrar_por_tags(lista, tag):
    tag_norm = tag.strip().lower()
    encontrado = False
    for post in lista:
    #lista temporal para poder normalizar los tags
        tags_lista_temporal = [t.lower() for t in post['tags']]
        if tag_norm in tags_lista_temporal:
            print("-" * 24)
            print(f"Titulo: {post['titulo']}")
            encontrado = True
    if not encontrado:
        print("no hay coincidencias")