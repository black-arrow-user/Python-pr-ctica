total_creeps= 0
print("---CONTADOR DE CREEPS")
for i in range(3):
    creeps_ola = int(input(f"Cuantos creeps mataste en la oleada {i+1}?"))

    total_creeps = total_creeps + creeps_ola
print(f"felicidades mataste un total de {total_creeps} creeps")
#Contador de Creeps: Usa un for para pedir cuántos creeps mataste en 5 oleadas. Muestra la suma total.