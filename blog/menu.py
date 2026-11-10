def mostrar_menu():
    print("---MENU DEL BLOG---")
    print("1.Listar posts")
    print("2.Buscar por titulo")
    print("3.Filtrar por tags")
    print("4.Validar post")
    print("5.Salir")
    while True:
        entrada = input("seleccione una opcion: ").strip()
        try:
            opcion = int(entrada)
            if 1 <= opcion <= 5:
                return opcion    
            else:
                print("ingrese un numero del 1 al 5")  
        except ValueError:
            print("ingrese un numero valido")