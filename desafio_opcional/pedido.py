from te import Te
from os import system
system("cls")
sabor = int(input("Ingrese el numero que corresponda para escoger el sabor \n1: Té negro\n2: Té verde\n3: Agua de hierbas.\n"))
tamano = int(input("ingrese el tamaño de la bolsa (300 o 500 gramos)\n"))

if sabor == 1: 
    tipoTe = "Té negro"
elif sabor == 2: 
    tipoTe = "Té Verde"
else: 
    tipoTe = "agua de hierbas"
    
print (" ----- PEDIDO ----- ")
print("")
print ("Sabor:",tipoTe)
print ("Formato:",tamano,"gramos")
print ("Precio:",Te.calcularPrecio(tamano),"pesos")
print ("tiempo:",Te.tiempoPreparacion(sabor)[0],"minutos")
print ("recomendación:",Te.tiempoPreparacion(sabor)[1])
print("")
print (" ----- FIN PEDIDO ----- ")

