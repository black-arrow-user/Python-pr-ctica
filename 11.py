print("LOG DE DAÑO CRITICO")
for i in range(5):
    daño = int(input(f"Ingresa valor de daño recibido numero {i}"))
if daño > 100 :
    with open("criticos.txt", "a") as archivo :
            archivo.write(f"{daño}\n")
else :
    print(daño)        
    #Log de Daño Crítico: Si el daño ingresado es $> 100$, guárdalo en criticos.txt. Si no, solo muéstralo.