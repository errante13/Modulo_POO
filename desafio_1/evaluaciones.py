#para limpipar la consola (me aburrí de estar escribiendo clear)
from os import system
from pizza import Pizza

system("cls")

#atributos de clase Pizza
print(" ")
print("--- LISTA DE INGREDIENTES PARA LA PIZZA ---")
print(Pizza.lista_vegetales)
print(Pizza.lista_proteina)
print(Pizza.masa)
print("--- LISTA DE ATRIBUTOS---")
print(Pizza.ingredientes)
print(Pizza.tamanio)
print(Pizza.precio)

#prueba el metodo estatico validar en Clase Pizza
print("--- VALIDACIÓN METODO ESTATICO  ---")
print(Pizza.validar("salsa de tomate",["salsa de tomate", "salsa bbq"]))

#se crea instancia de pizza 
pz = Pizza()

#ejecución del metodo Hacer pedidos
print("--- PRUEBA DE METODO CON LA INSTANCIA ---")
print(pz.hacerPedido())
print("--- PRUEBA DE METODO SIN INSTANCIA ---")
print(Pizza.hacerPedido())

