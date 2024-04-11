from te import Te
#a 
te_uno = Te()
te_dos = Te()
#b  
print(type(te_uno))
print(type(te_dos))
#C
print(te_uno.duracion)
print(te_dos.duracion)
#D 
if te_uno.duracion == te_dos.duracion:
    print("el tipo de datos es igual\n")
else: 
    print("los tipos de datos son diferentes\n")
