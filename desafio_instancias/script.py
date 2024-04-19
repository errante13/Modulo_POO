import os,json 
from usuario import Usuario

os.system("cls")

# archivo =open(os.path.abspath('usuarios.txt'))

with open("usuarios.txt", "r") as usuarios:
    #print(usuarios.redlines())
    linea = usuarios.readline()
    #paso 7 se crea lista para almacenar usuarios
    lista_usuarios=[]
    #paso 3 controlar la exepción 
    while linea:
        try: 
            #paso 2 transformar texto en json
            usuario_dicc = json.loads(linea)
            #print(usuario_dicc)
            #paso 6 crear una instancia de usuario
            instancia_usuario = Usuario(
                usuario_dicc["nombre"],
                usuario_dicc["apellido"],
                usuario_dicc["email"],
                usuario_dicc["genero"],
            )
            lista_usuarios.append(instancia_usuario)
        except Exception as error:
            # paso 4 imprimir el error    
            print("el error es: ", error)
            # paso 5 guardar el error en un archivo log 
            with open("error.log","a+") as log:
                print(log)
                log.write(f"el error es: {error}\n")
        finally:
            #paso 8 posicionar en la siguiente linea
            linea = usuarios.readline()
            
                
print("contenido de la lista", lista_usuarios)           
        