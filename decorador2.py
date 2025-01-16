#DECORADOR  

#Crear Decorador
def funcion_decoradora(funcion_parametro):
    #Primero entro aqui
    def funcion_interna():
        # Acciones adicionales que decoran 
        print("Vamos a realizar un calculo:")
        funcion_parametro()     #Llamadad a funcion recibida como parametro
        #Acciones adicionales que decoran
        print ("Hemos terminado el calculo")

    return funcion_interna


# Cuando se produzca la llamada a la funcion suma tiene mas acciones adicionales

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()

resta()

