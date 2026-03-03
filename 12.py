lista_heroes =["balanar", "slark", "razor", "shadowfiend", "viper"]
print("FILTRO DE NOMBRES LARGOS")
for nombre in lista_heroes:
    if len(nombre) > 5 :
     print(f"heroe filtrado : {nombre} (tiene {len(nombre)} letras)")
     #Filtro de Nombres: De una lista de héroes, imprime solo los que tengan más de 5 letras (len > 5).