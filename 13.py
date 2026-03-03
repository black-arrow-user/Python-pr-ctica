print("---VENDEDOR DE ITEMS---")
lista_item = ["rapier","monkey","satanic","bkb","skady"]
while True:
    print(f"\n tu inventario actual: {lista_item}")
    accion = input("Que quieres hacer comprar, vender o salir?").lower()   
    if accion == "salir" :
        print("vuelve cuando quieres")
        break
    elif accion == "comprar" :
        nuevo_item = input("Cual de los items quieres comprar ?")
        lista_item.append(nuevo_item)
        print(f" felicidades has comprado {nuevo_item}")
    elif accion == "vender" : 
        if len(lista_item) > 0:
            item_vendido = lista_item.pop()  
            print(f" felicidades has vendido tu ultimo item {item_vendido}")
        else :
            print("No tienes nada para vender! tu mochila esta vacia")
    else :
        print("opcion no valida. escribe comprar, vender o salir.")    
        #Vendedor de Ítems: Un menú para "comprar" (append) o "vender" (pop) ítems de tu inventario.    

