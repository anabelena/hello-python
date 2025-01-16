diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

#palabra reservada para ver si existe 
print('a' in diccionario)

""" 
#Obtener valor de KEY
valor = diccionario['b']
print(valor)

"""
#GET
# .get(key, return)  #by default NONE
valor = diccionario.get('b','la llave no existe en el diccionario')
valor = diccionario.get('e', None)

#setdefault
valor= diccionario.setdefault('e',5)


print(valor)
print(diccionario)

