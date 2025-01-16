#Docstring
#__doc__ (Modulos,Clases,Metodos,Funciones)
#Comentario que se coloca en la primera linea de codigo de nuestra FUNCION.

def suma(numero1,numero2):
    """
    La funcion realiza una sumatoria de dos numeros enteros.
    
    Argumentos:
    numero1 (int)
    numero2 (int)

    Se retorna la suma de los parametros.

    TODO: 
        *
    """
    return numero1 + numero2


print(suma(1,3))


print(suma.__doc__) #Atributo DOC que solo lo poseen los objetos DOCUMENTABLES.
print(help(suma))   #Documentacion de la funcion

#OJO -> Objetos documentables como: MODULOS, CLASES, METODOS, FUNCIONES.

