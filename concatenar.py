#concatenacion de cadenas
nombre = 'Ana Belen'
apellido = 'Arista'

#Operador + para unir mas de una cadena
print('Sra ' + nombre + ' ' + apellido + '.')


#Utilizando un STRING BASE
#nombre_completo = 'Mr. %s %s %s.' %(nombre,apellido,'Perez')
#print(nombre_completo)

"""
#Metodo Format
#Placeholders son reemplazados por valores entre parentesis.
nombre_completo = 'Mr. {} {} {}.' .format(nombre,apellido,'Huamonte')
print(nombre_completo)
"""

#FSTRING  (interpolacion)
#Permiten generar nuevos strings a partir de otros.
nombre_completo = f'Mr. {nombre} {apellido} {"Perez"}'
print(nombre_completo)

#Funcion PRINT
#Permite imprimir en consola diferentes valores, cualquier objeto.
print(nombre,apellido,'Perez',True,2.364,sep='-')


