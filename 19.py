#Bucle de Nivel (XP):
nivel_actual= 1
experiencia_actual= 0
limite_xp = 1000
while True:
    print(f"\nNivel: {nivel_actual}  |  {experiencia_actual}/{limite_xp}")
    opcion = input(f"XP actual: {experiencia_actual}/{limite_xp}. presiona ENTER para sumar 300 puntos de XP")
    experiencia_actual += 300 
    if experiencia_actual >= limite_xp :
        nivel_actual = nivel_actual + 1
        experiencia_actual = experiencia_actual - limite_xp
        print(f"subiste el nivel ({nivel_actual}) y te sobra {experiencia_actual} XP para el siguiente nivel")
        with open("progreso.txt","a") as archive:
            archive.write(f"\nsubiste a {nivel_actual}")
    elif opcion == "salir":
        break        
            
