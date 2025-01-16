
def pares():    #Generador -> Lazy Iterator
    for numero in range(0,100,2):

        yield numero    #La funcion suspende su ejecucion.

        print('Se reanuda la ejecucion')

generador = pares()


while True:
    try:
        par = next(generador)
        print(par)

    except StopIteration:
        print('El generador finalizo')
        break


"""

generador = pares()     #Almaceno generador o resultado de funcion en una variable

print(next(generador))

print(next(generador))

print(next(generador))

print('Ejecutar codigo')

print(next(generador))


"""


