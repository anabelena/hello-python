#Funciones anidadas/ Funciones que retornan funciones

def choose_num(num):                #Funcion Padre

    def opt_1():                    #Funcion anidada 1
       
        return'You choose 9.'

    def opt_2():                    #Funcion anidada 2
     
        return'You didn\'t choose 9.'

    if num == 9:                    #Condicional
     
        return opt_1                #Retorna la funcion anidada 1

    else:
  
        return opt_2                #Retorna la funcion anidada 2



#Variable que recibira el resultado de la FUNCION PADRE
funcionresultado = choose_num(9)  #Variable que almacena ya sea opt_1 or opt_2


#Para ejecutar la funcionresultado tengo dos opciones
# 1 ->
# Ejecutarla y ya que tiene return almacenarla en otra variable y asi visualizar el resultado

mivariable = funcionresultado()
print(mivariable)

#2->
# Ejecutarla e imprimir el output directamente usando PRINT
print(funcionresultado())


