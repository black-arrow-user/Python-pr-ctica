print("--PROMEDIO KDA--")
kills = int(input("Cuantas kills tienes"))
deaths = int(input("Cuantas veces haz muerto"))
assists = int(input("Cuantas asistencias tienes"))
if deaths == 0 : deaths = 1
promedio_kda = int((kills + assists)/ deaths)
print(f"Tu primedio KDA es {promedio_kda}")
#Promedio de KDA: Pide Kills, Deaths y Assists. Calcula el promedio: $(K+A)/D$.