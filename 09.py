print("---ELIMINAR ITEM---")
lista = ["tango", "botas", "varita", "bracer", "manto", "polvo"]
for i in range(len(lista)) :
    print(f"Slot {i}: {lista[i]}")
posicion = int(input("que numero de slot quieres vaciar"))
item_eliminado = lista.pop(posicion)
print(f"\nHas descartado : {item_eliminado}!")
print("---Inventario actualizado---")
print(lista)
#Eliminar Ítem (Slots): De una lista de 6 ítems, pide el número de slot (índice) para borrarlo con .pop().