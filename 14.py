print("---GUARDADO HISTORIAL PRO---")
nombre = input("dame el nombre de un heroe")
resultado_partida = input("La partida fue Ganada o Perdida")
if resultado_partida == "Ganada" :
    with open("historial.txt","a") as archive:
        archive.write(f"\nHEROE {nombre} | RESULTADO: {resultado_partida}")
elif resultado_partida == "Perdida" :
    with open("historial.txt","a") as archive:
        archive.write(f"\nHEROE {nombre} | RESULTADO: {resultado_partida}")        
else :
    print("Por favor colocar solo Ganada o Perdida") 
with open("historial.txt","r") as archive :
    contenido = archive.read()
    print(contenido)
    #Guardado de Historial: Pide Héroe y Resultado (G/P). Guárdalo con formato profesional en historial.txt.