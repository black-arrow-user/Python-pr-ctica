print("---MOCHILA SOPORTE---")
while True:
    print("-Opciones- : ")
    items_soporte = ["wards","smoke","dust"]
    inventario =[]
    print("wards\nsmoke\ndust\nmostrar mochila\n")
    items = input(" Hola me indicas que item de soporte tienes?")
    if items in items_soporte :
        inventario.append(items) 
        with open("listaitemssoporte.txt","a") as archivo:
            archivo.write(f"{items}\n")
        print(f"{items} añadido a tu mochila\n")
    elif items == "salir" : break
    elif items == "mostrar mochila" :
        print("--MOCHILA--")
        try:
            with open("listaitemssoporte.txt","r") as archivo:
                print(archivo.read())
        except : FileNotFoundError
        print("Aun no hay compras registradas")
    else :
     print("opcion no valida, por favor escriba una opcion.")
     #Mochila de Soporte: Usa un while para pedir ítems (wards, smoke). Guárdalos en una lista hasta escribir "listo".



