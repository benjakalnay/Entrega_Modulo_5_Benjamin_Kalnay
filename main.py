from blog.modelos import Autor, Post, Blog
from blog.menu import mostrar_menu
from blog.datos import cargar_post, guardar_post

def main():
    posts_cargados = cargar_post()
    mi_blog = Blog()
    mi_blog.posts = posts_cargados

    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            mi_blog.listar_posts()            
        elif opcion == 2:
            titulo = input("ingrese un titulo: ")
            resultado = mi_blog.buscar_por_titulo(titulo)
            if len(resultado) > 0:
                for post in resultado:
                    print(post)
            else:
                print("no se encontraron post con ese titulo, vuelva a intentarlo")
        elif opcion == 3:
            tag = input("ingrese un tag: ")
            resultado_tags = mi_blog.filtrar_por_tags(tag)
            if len(resultado_tags) > 0:
                for post in resultado_tags:
                    print(post)
            else: 
                print("no se encontraron coincidencias")
        elif opcion == 4:
            nombre = input("ingrese sus datos, nombre: ")
            bio = input("bio: ")
            autor = Autor(nombre, bio)
            titulo_nuevo = input("titulo: ")
            contenido_nuevo = input("contenido: ")
            tags_nuevo = input("tags: ")
            tags_lista =  [t.strip() for t in tags_nuevo.split(",")]
            estado_nuevo = input("estado: ")
            mi_blog.crear_post(titulo_nuevo, contenido_nuevo, autor, tags_lista, estado_nuevo)
            print("post creado con exito")
        elif opcion == 5:
            print("----validando posts----")
            mi_blog.validar_todos()
        elif opcion == 6:
            print("gracias por utilizar el blog, nos vemos pronto!;)")
            guardar_post(mi_blog.posts)
            break

if __name__ == "__main__":
   main()



