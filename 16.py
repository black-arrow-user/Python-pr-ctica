lista_items = []
print("Simulador de Courier:")
while True :
    items = input("Que items tienes o si no tienes escribe salir")
    if items == "salir": 
        break    
    elif len(items) > 0 :
        lista_items.append(items)
        print(lista_items)
    else :
        print("por favor colocar una opcion")  

    accion = input("Que quieres hacer enviar,vaciar o salir")
    if accion == "enviar" :
        with open("entrega.txt","a") as archivo:
            archivo.write(f"{lista_items}\n")
            print("objeto enviado excitosamente")
    elif accion == "vaciar":
        lista_items.clear()
        print(f"lista vaciada {lista_items}") 
    elif accion == "salir":
        break         
    else :
        print("por favor colocar una opcion")  


