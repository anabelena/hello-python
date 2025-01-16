e = 'e' #Variable global

def funcion_principal():
    a = 'a'     #Variable local bloque funcion_principal
    b = 'b'     #Variable local
    
    def funcion_anidada():
        global c
        c = 'c' #Variable local del bloque funcion_anidada
        nonlocal b
        b = 'Cambio de valor'
        print(a)
        print(b)
        print(id(b)) 
        print(e) #Variable global utilizada en bloque

    funcion_anidada()

    print(b)
    print(id(b))
    print(c) #Variable global definida en funcion anidada
    
funcion_principal()

