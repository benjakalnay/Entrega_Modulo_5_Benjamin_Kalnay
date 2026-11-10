from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts
from blog.operaciones import buscar_por_titulo
from blog.operaciones import filtrar_por_tags
from blog.validaciones import validar_post

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            titulo = input("ingrese un titulo: ")
            buscar_por_titulo(posts, titulo)
        elif opcion == 3:
            tag = input("ingrese un tag: ")
            filtrar_por_tags(posts, tag)
        elif opcion == 4:
            print("---validando posts---")
            for post in posts:
                if validar_post(post):
                    print(f"Post id: {post['id']} paso la validación correctamente")
        elif opcion == 5:
            print("gracias por utilizar el blog, nos vemos pronto!;)")
            break

if __name__ == "__main__":
   main()


