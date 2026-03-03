print("--- CALCULADORA DE MANA PRO ---")
print("Hechizos: Epicentro, Agujero negro, Baile de las sombras")
grupo_hechizo = ["Baile de las sombras", "Epicentro", "Agujero negro"]
hechizo = input("¿Que hechizo vas a usar? ")
if hechizo in grupo_hechizo :
 mana_actual = int(input("¿Cuanta mana tienes? "))
costo = 0
if hechizo == "Epicentro":
    costo = 225
elif hechizo == "Agujero negro":
    costo = 300
elif hechizo == "Baile de las sombras":
    costo = 175
else:
    print("Opción no válida") 
if costo > 0:
    if mana_actual >= costo:
        print(f"¡Tienes la mana suficiente para {hechizo}, úsalo!")
    else:
        falta = costo - mana_actual
        print(f"Te falta {falta} de mana para usar {hechizo}. ¡Ve a la fuente!")
else :    
    print("Opcion no valida, por favor volver a intentarlo")
    #Calculadora de Mana: Pide el costo de un hechizo y el mana actual. Di si puede lanzarlo o si le falta.
        