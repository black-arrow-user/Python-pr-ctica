print("---CALCULADORA DE MANA---")
grupo_hechizo = ["Baile de las sombras", "Epicentro", "Agujero negro"]
for i in range(len(grupo_hechizo)) :
    print(f"hechizo {i}: {grupo_hechizo[i]}")
hechizo = int(input("Que hechizo vas a usar?"))
if hechizo in grupo_hechizo : 
 mana = int(input("Cuanta mana tienes ?"))
 if hechizo == "Epicentro" :
     if mana >= 225 :
        print("tienes la mana suficiente, usalo!")
     else :
        print("te falta mana, ve a la fuente!.")    
 elif hechizo == "Agujero negro" :
     if mana >=300 :
        print("tienes la mana suficiente, usalo!")
     else :
        print("te falta mana, ve a la fuente!.")
 elif hechizo == "Baile de las sombras" :
     if mana >=175 :
        print("tienes la mana suficiente, usalo!")
     else :
        print("te falta mana, ve a la fuente!.")
else :
   print("Opcion no valida, por favor volver a intentarlo")
#Calculadora de Mana: Pide el costo de un hechizo y el mana actual. Di si puede lanzarlo o si le falta.




