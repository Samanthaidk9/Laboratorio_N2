import json


def dow_fv():
    try:
        with open("favoritos.json", "r") as archivo:
            favoritos = json.load(archivo)
    except FileNotFoundError:
        favoritos = []
    return favoritos


def guardar_fav(favoritos):
    with open("favoritos.json", "w") as archivo:
        json.dump(favoritos, archivo, indent=4)


def agregar_fav():
    titulo = input("Digite el título del favorito: ")
    url = input("Digite la URL del favorito: ")
    comentario = input("Digite un comentario: ")

    favorito = {
        "Título": titulo,
        "URL": url,
        "Comentario": comentario
    }

    favoritos.append(favorito)
    guardar_fav(favoritos)
    print("Favorito agregado.")


def eliminar_fav():
    titulo = input("Digite el título del favorito a eliminar: ")

    for favorito in favoritos:
        if favorito["Título"] == titulo:
            favoritos.remove(favorito)
            guardar_fav(favoritos)
            print("Favorito eliminado.")
            return

    print("No se encontró ese título.")


def modificar_fav():
    titulo_eliminar = input("Digite el título del favorito a modificar: ")

    for favorito in favoritos:
        if favorito["Título"] == titulo_eliminar:
            nuevo_titulo = input("Digite el nuevo título: ")
            nuevo_url = input("Digite el nuevo URL: ")
            nuevo_comentario = input("Digite el nuevo comentario: ")

            favorito["Título"] = nuevo_titulo
            favorito["URL"] = nuevo_url
            favorito["Comentario"] = nuevo_comentario

            guardar_fav(favoritos)
            print("Favorito modificado.")
            return

    print("No se encontró ese título.")


def ver_favoritos():
    if favoritos:
        print("Lista:")
        for favorito in favoritos:
            print("- Título:", favorito["Título"])
            print("  URL:", favorito["URL"])
            print("  Comentario:", favorito["Comentario"])
            print()
    else:
        print("No hay favoritos almacenados.")


favoritos = dow_fv()


while True:
    print("***** Menú Principal *****")
    print("1. Agregar favorito")
    print("2. Eliminar favorito")
    print("3. Modificar favorito")
    print("4. Ver la lista de favoritos")
    print("5. Salir")

    opcion = input("Ingrese la opcion: ")

    if opcion == "1":
        agregar_fav()
    elif opcion == "2":
        eliminar_fav()
    elif opcion == "3":
        modificar_fav()
    elif opcion == "4":
        ver_favoritos()
    elif opcion == "5":
        print("¡error!")
