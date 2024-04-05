#para limpipar la consola (me aburrí de estar escribiendo clear)
from os import system
from pizza import Pizza

system("cls")

#atributos de clase Pizza
print(Pizza.lista_vegetales)
print(Pizza.lista_proteina)
print(Pizza.masa)

#prueba el metodo estatico validar en Clase Pizza
print(Pizza.validar("salsa de tomate",["salsa de tomate", "salsa bbq"]))

#se crea instancia de pizza 
pz = Pizza

#ejecución del metodo Hacer pedidos
print(pz.hacerPedido())

print(Pizza())