#LLAVES 
diccionario = {'a':1,'b':2,'c':3,'d':4}

#keys <- retorna un objeto "dict_keys" con todas las llaves del diccionario
llaves = tuple(diccionario.keys())
print(llaves)

#values <- retorna un objeto "dict_values" con la lista de valores dentro del diccionario
valores = tuple(diccionario.values())
print(valores)

#items <- retorna un objeto "dict_items" llave, valor
elementos = tuple(diccionario.items())
print(elementos)


#Convertir elementos a tuplas para que no puedan ser modificados.
#De esta forma evitamos errores