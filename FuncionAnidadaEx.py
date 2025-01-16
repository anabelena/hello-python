e = 'e' #Variable GLOBAL, puede ser utilizada en cualquier parte del programa.

def funcion_padre():
    a = 1 #Variable local
    b = 2 #Variable local pero por jerarquia pueden ser utilizadas en bloques inferiores.
    x1 = 20
    print(a)
    print(id(a))
    def funcion_hijo():         
        c = 'Hola como estas'   #Variable local = Creada dentro de un bloque solo pueden ser utilizadas en ese bloque
        a = 10000       
        x2 = 50
        x3 = x1 +x2
        x4 = a
        print(x3)
        print(x4)
        print(id(a))
    print(x1)
    funcion_hijo()

print(e)   
funcion_padre()

















































































    
