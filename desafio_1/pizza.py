import ingredientes
class Pizza:
    
    # lista ingredientes
    lista_vegetales = ["tomate", "aceitunas", "champiñones"]
    masa = ["delgada", "gruesa"]
    lista_proteina = ["pollo", "vacuno", "carne vegetal"]
    
    #ATRIBUTOS PIZZA
    ingredientes =[]
    precio = 10000
    tamanio = "familiar"
   
      
    # METODO DE VALIDACION
    @staticmethod
    def validar(eleccion, opciones):
        if eleccion in opciones:
            return True
        return False

    def hacerPedido(self):
        validos =[]
                
        # ingrediente proteico
        proteina = input(f"favor ingresar un ingrediente de la lista {ingredientes.lista_proteina} \n").lower()
        # print(proteina) (linea para probar codigo)
        # validamos que corresponda la opción corresponda
        
        if  self.validar(proteina, ingredientes.lista_proteina):
            self.ingredientes.append(proteina)
            validos.append(True)
            # print(validos) // pruebas de codigo
            print("ingrediente agregado\n")
            # print(self.validar) //pruebas de codigo
        else:
            # print(self.validar) //pruebas de codigo
            validos.append(False)
            print("ingrediente no valido\n")

        # se agrega primer Ingrediente vegetal
        vegetal_uno = input(f"favor ingresar un ingrediente de la lista {ingredientes.lista_vegetales}\n").lower()
        # validamos que corresponda la opción corresponda
        if self.validar(vegetal_uno, ingredientes.lista_vegetales):
           self.ingredientes.append(vegetal_uno)
           validos.append(True)
           print("ingrediente agregado\n")
        else:
            print("ingrediente no valido\n")
            validos.append(False)

        # se agrega segundo Ingrediente vegetal
        vegetal_dos = input(f"favor ingresar un ingrediente de la lista {ingredientes.lista_vegetales}\n").lower()
        # validamos que corresponda la opción corresponda
        if self.validar(vegetal_dos, ingredientes.lista_vegetales):
            self.ingredientes.append(vegetal_dos)
            validos.append(True)
            print("ingrediente agregado\n")
        else:
            validos.append(False)
            print("ingrediente no valido\n")

        # se agrega MASA
        masa = input(f"favor ingresar una masa de la lista {ingredientes.masa}\n").lower()
        # validamos que corresponda la opción corresponda
        if self.validar(masa, ingredientes.masa):
            self.ingredientes.append(masa)
            validos.append(True)
            print("ingrediente agregado\n")
        else:
            validos.append(False)
            print("ingrediente no valido\n")
        
        #----- VALIDACIÓN DE LA PIZZA CORRECTA ---
         
        if False not in validos:
            print(f"el pedido es válido, \n los ingredientes de la pizza son: {self.ingredientes}\n")
            #return ingredientes
        else:
            print("el pedido no es válido ")
            return self.ingredientes
        
# pz.hacerPedido()
