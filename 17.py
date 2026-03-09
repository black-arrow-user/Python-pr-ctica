
print("Sistema de Ban-List:")
while True:
    nombre = input("Cual es tu nick de jugardor")
    if nombre == "salir":
        break
    estado = input("Cual fue el motivo de reporte(toxico,trampa o otra cosa) ?")
    if estado == "toxico" :
        with open("ban_list.txt", "a") as archive:
            archive.write(f"jugador {nombre} | reportado por {estado}\n")
            print(f"Reportado por {estado}")
    elif estado == "trampa" :
        with open("ban_list.txt", "a") as archive:
            archive.write(f"jugador {nombre} | reportado por {estado}\n")
            print(f"Reportado por hacer {estado}")
    elif estado == "otra cosa":
        print(f"fuiste reportado por {estado}")        
    elif estado == "salir" : 
        break            