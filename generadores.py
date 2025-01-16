#Generadores: Permiten extraer valores de una funcion y almacenarlos de uno en uno en objetos iterables.
# Sin necesidad de almacenar todos a la vez en la memoria RAM

#YIELD -> Permite retornar valores y suspender la ejecucion de la funcion 
def pares():    #GENERADOR -> Lazy iterator

    for numero in range(0,10,2):
        
        print('Aqui vamos ')

        yield numero #suspenderemos la ejecucion de la funcion
                    
        print('Se reanuda la ejecucion')


for par in pares():
    print (par)



