# LISTAS PYTHON

#INDICES            0        1        2      3      4
lista_cursos = ['Python','Django','Flask','Ruby','Java','Rust']
#INDICES           -5      -4       -3      -2     -1

# CREANDO LISTA
lista_nombre = ['Ana','Belen','Karlos','Enrique','Elena']

# INSERTANDO VALORES -> .append() adds a single element at the end of the list 
lista_nombre.append('Lola')
lista_nombre.append('Concepcion')
lista_nombre.append('Juan')
print(lista_nombre)

#INSERTANDO VALORES -> .extend() adds multiple elements to the list
lista_nombre.extend(['otro','otromas','unomas'])
print(lista_nombre)
 
#INSERTANDO VALORES -> .insert() add new element in a speific index
lista_nombre.insert(2,'Judith')
print(lista_nombre)

#  ACTUALIZAR elementos de una lista indicando INDICE
lista_nombre[2] = 'Anita'
print(lista_nombre)

#OBTENER elementos con respecto a sus indices
primer_nombre = lista_nombre[0] 
print(primer_nombre)


#OBTENER ULTIMO ELEMENTO o leer de DERECHA A IZQUIERDA
#Utilizo INDICE NEGATIVO
ultimo_nombre = lista_nombre[-1]
print(ultimo_nombre)


#ELIMINAR ELEMENTO 
# Metodo remove()
lista_nombre.remove('Juan')
print(lista_nombre)

# Palabra reservada del 
del lista_nombre[0]
print(lista_nombre)

# Metodo clear() -> delete all the elements
lista_nombre.clear()

# LONGITUD DE LA LISTA
# len()
print(len(lista_nombre))