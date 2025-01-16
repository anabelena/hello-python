#TRABAJANDO METODOS DE LISTAS
lista = [8,90,1,5,44,132,600,3,4]
print(lista)

#ORDENANDO elementos de una lista
# .sort() ordena la lista de forma ascendente, de menor a mayor
lista.sort()
print(lista)

lista.sort(reverse=True) #ordenamiento descendente 
print(lista)

#OBTENER Numero Menor y Mayor
lista.sort()
print(lista[0]) #min
print(lista[-1]) #max

#Funcion Min and Max
print(min(lista))
print(max(lista))

#Palabra reservada IN para ver si elemento se encuentra en lista
print(20 in lista)
print(5 in lista)
print(11 not in lista)
print(8 not in lista)

# .index()  retorna el indice de un valor en una lista
# retorna siempre el primer valor en caso de existir mas de un valor igual 
index = lista.index(44)
print(index)

