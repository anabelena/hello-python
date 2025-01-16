#Funciones pueden retornar otras funciones
#Funciones pueden ser tratadas como argumentos
#Funciones pueden ser tratadas como variables

#Retornar funciones
def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos en el curso de python.')

    return mostrar_mensaje

respuesta = saludar()

respuesta()