#Eliminar elementos

diccionario = {'a':1,'b':2,'c':3,'d':4}

#DEL -> palabra reservada
del diccionario['a']  #1

#METODO POP
#retorna el valor a eliminar
valor = diccionario.pop('b') #2

#METODO CLEAR
#Elimina todos los elementos
diccionario.clear()          #3


#Imprimir
print(valor)
print(diccionario)
