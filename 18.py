tienda = {
    "daga" : 2150,
    "bkb" : 4250,
    "monkey": 4850
}
inventario = []
print("---Calculadora de Compra Selectiva:---")
oro = int(input("Cuanto oro tienes?"))

while oro > 0 :
 print(f"\nTIENDA DISPONIBLE: (tu oro: {oro})") 
 for item, precio in tienda.items():
     print(f"*{item} - valor: {precio}")
 seleccion = input("\nQue item quieres comprar? (o escribe salir)(o escribe inventario para ver tu compras) ").lower()
 if seleccion == "salir":
    break
 if seleccion in tienda:
    precio_item = tienda[seleccion]
    if oro >= precio_item:
       oro =  oro - precio_item
       inventario.append(seleccion)
       print(f"Compraste {seleccion}. te queda {oro} de oro")
    else:
       print(f"No te alcanza. te faltan {precio_item - oro} monedas.")
 if seleccion == "inventario":
    print(inventario)        
 else:
    print("ESE ITEM NO ESTA EN AL TIENDA. REVISA EL NOMBRE")
print(f"Saliendo... Oro final: {oro}")    
