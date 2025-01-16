#Creacion de Funciones
#Dentro de una funcion se pueden llamar a mas funciones. Input, Print, etc.

def suma():
    numero1= input('Ingresa el primer numero entero') #string
    numero2= input('Inresa el segundo numero entero')
    valor1 = int(numero1)
    valor2= int(numero2)
    resultado = valor1 + valor2
    print(resultado)

#Invocar a la funcion
suma()

#Argumentos, parametros, VALORES DE ENTRADA
def sumatoria(n1,n2):
    total = n1 + n2
    #print(total)
    return total,'la funcion retona dos valores'    #genera una tupla
1

numero1= int(input('Ingresa un numero entero')) #string
numero2= int(input('Ingresa un numero entero'))

resultado = sumatoria(numero1,numero2)
print(resultado)

#Palabra reservada: RETURN

