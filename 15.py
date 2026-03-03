print("--Verificador de Inventario Lleno:--")
lista_item = []
while True : 
   item = input("Que item quieres agregar a tu lista")
   if len(lista_item) > 5 :
      print("¡Inventario lleno! No puedes cargar más")
      break
   else :
      lista_item.append(item)
      print(f"item {item} agregado exitosamente")
      print(lista_item)      
      #Verificador de Límite: Un while para añadir ítems que se detenga automáticamente si la lista llega a 6 elementos.
