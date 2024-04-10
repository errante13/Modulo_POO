class Celular ():
    def __init__(self,tamanio=0):
        self.tamanio = tamanio
        
    def __eq__(self, other):
        print(self.tamanio,other.tamanio)
        return self.tamanio == other.tamanio    
        
android = Celular(16)
iphone = Celular(16)


print(android)#<__main__.Celular object at 0x000001E82FC75E50>
print(iphone)#<__main__.Celular object at 0x000001E82FC75F40>

print(android == iphone) #False

windowp = android
print(windowp)#<__main__.Celular object at 0x000001E82FC75E50>

