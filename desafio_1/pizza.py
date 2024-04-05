class Pizza:
    
    # lista ingredientes
    lista_vegetales = ["tomate", "aceitunas", "champiñones"]
    masa = ["delgada", "gruesa"]
    lista_proteina = ["pollo", "vacuno", "carne vegetal"]
  
   #ATRIBUTOS PIZZA
    
    
    # METODO DE VALIDACION
    @staticmethod
    def validar(eleccion, opciones):
        if eleccion not in opciones:
            return False
        return True

    def hacerPedido():
        validos =[]
        ingredientes =[]
        
        # ingrediente proteico
        proteina = input(f"favor ingresar un ingrediente de la lista {Pizza.lista_proteina} \n").lower()
        # print(proteina) (linea para probar codigo)
        # validamos que corresponda la opción corresponda
        
        if Pizza.validar(proteina, Pizza.lista_proteina):
            ingredientes.append(proteina)
            validos.append(True)
            # print(validos) // pruebas de codigo
            print("ingrediente agregado")
            # print(self.validar) //pruebas de codigo
        else:
            # print(self.validar) //pruebas de codigo
            validos.append(False)
            print("ingrediente no valido  ")

        # se agrega primer Ingrediente vegetal
        vegetal_uno = input(f"favor ingresar un ingrediente de la lista {Pizza.lista_vegetales}").lower()
        # validamos que corresponda la opción corresponda
        if Pizza.validar(vegetal_uno, Pizza.lista_vegetales):
            ingredientes.append(vegetal_uno)
            validos.append(True)
            print("ingrediente agregado")
        else:
            print("ingrediente no valido  ")
            validos.append(False)

        # se agrega segundo Ingrediente vegetal
        vegetal_dos = input(f"favor ingresar un ingrediente de la lista {Pizza.lista_vegetales}").lower()
        # validamos que corresponda la opción corresponda
        if Pizza.validar(vegetal_dos, Pizza.lista_vegetales):
            ingredientes.append(vegetal_dos)
            validos.append(True)
            print("ingrediente agregado")
        else:
            validos.append(False)
            print("ingrediente no valido ")

        # se agrega MASA
        masa = input(f"favor ingresar una masa de la lista {Pizza.masa}").lower()
        # validamos que corresponda la opción corresponda
        if Pizza.validar(masa, Pizza.masa):
            ingredientes.append(masa)
            validos.append(True)
            print("ingrediente agregado")
        else:
            validos.append(False)
            print("ingrediente no valido ")

        if False not in validos:
            print(f"los ingredientes de la pizza son: {ingredientes}\n")
            #return ingredientes
        else:
            print("el pedido no es válido ")
            return ingredientes

# pz.hacerPedido()
