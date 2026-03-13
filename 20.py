#El Gran Resumen: Pide todos los datos de una partida e imprime una "Ficha Técnica" completa, guardándola en un archivo con el nombre del héroe.
nombre = input("Cual es el nombre del heroe?")
kills = int(input("Cuantos kills logro en la partida?"))
muertes = int(input("Cuantas veces murio en la partida?"))
asistencias = int(input("Cuantas veces asistio a su equipo?"))
oro = int(input("Oro final :"))
if muertes == 0:
    KDA = kills + asistencias
else:    
    KDA = (kills + asistencias/muertes)

ficha = f"""
         FICHA DE PARTIDA :{nombre.upper()}

kills: {kills}  |  Muertes: {muertes}  |  Assists: {asistencias}
KDA TOTAL: {KDA:.2f}
ORO ACUMULADO: {oro}

"""
with open(f"{nombre}.txt","a") as archive:
    archive.write(ficha)
print(f"\nFicha tecnica creada con exito !")
print(f"Busca el archivo: {nombre}.txt") 