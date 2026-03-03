lista_heroes =[]
print("---Heroes favoritos---")
for i in range(3):
    heroe = input(f"Cuales son tu heroe favorito numero{i}:")
    lista_heroes.append(heroe)
    with open("heroes favoritos.txt","a") as archivo:
        archivo.write(f"{heroe}\n")
print("\n--- TU TOP 3 DE HEROES ---")
lista_heroes.reverse()
for h in lista_heroes:
    print(f"heroe top: {h}")
#Héroes Favoritos: Pide 3 nombres, guárdalos en una lista y luego imprímelos en orden inverso.

