#Generadores: Permiten extraer valores de una funcion y almacenarlos de uno en uno en objetos iterables.
# Sin necesidad de almacenar todos a la vez en la memoria RAM


"""
#Funcion para generar MULTIPLOS de 7
def generaMultiplos7(limite):
    numero = 1                  #Inicializo variable numero
    listanumeros=[]             #Creo variable tipo Lista "listanumeros"

    while numero <= limite:
        listanumeros.append(numero * 7) #Agrego multiplo a la lista
        numero = numero + 1

    return listanumeros     #Retorna toda la lista creada.

#Imprimir funcion 
print(generaMultiplos7(10))

"""

def generadorMultiplos7(limite):

    numero = 1          
    
    while numero <= limite:
        yield numero * 7    #Ceder. "Yield" genera un objeto iterable.
        numero = numero + 1 


obtieneMultiplo = generadorMultiplos7(5)  #Funcion no tiene return por lo que debo guardar resultado en VARIABLE

#print(obtieneMultiplo)

#for n in obtieneMultiplo:       #Generador nos permite obtener uno por uno
#   print(n)

#next() Retorna siguiente elemento de un objeto iterable

print(next(obtieneMultiplo))
print('Aca hay 300 lineas de codigo')
print(next(obtieneMultiplo))
print("estoy leyendo el objeto no la funcion")
print(next(obtieneMultiplo))
      
      #------IMPORTANTE------
# Generadores: Son mas eficientes que las funciones tradicionales.
# Muy utiles con listas de valores infinitos.
# Entre llamada y llamada, el objeto iterable entra en un estado de pausa.(Suspension)