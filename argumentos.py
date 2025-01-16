#ARGUMENTOS I
#Ejemplo
#Funcion print recibe n argumentos
print('a','b',12,148480)

def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([12,15,12,14,13,11])
print(resultado)


#POR CONVENCION TODOS LOS PARAMETROS CON * deben nombrarse args
def promedio2(*args): #tupla
    print(args)
    print(type(args))
    return sum(args) / len(args)

resultado = promedio2(12,15,14,15,16)
print(resultado)

#ARGUMENTOS II
#def combinacion(p1,p2,p3):
def combinacion(p1,p2,*args,p4=500):
    print(p1)
    print(p2)  
    print(args)
    print(p4)

combinacion(1,2,4,45,9,3,9,7,p4=1000)

#** diccionario 
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[11,18,13],belen=[12,13,19],karlos=[15,16,19])

def combinacion(*args,**kwargs):
    print(args)
    print(kwargs)


combinacion(1,2,3,4,5,ccdy=True,curso='Python')