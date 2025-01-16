#SCOPE
animal = 'Leon'   #Variable Global -> pueden ser utilizada dentro de cualquier  bloque
                  #-> Funcion, Condicion o Ciclo
def imprimir_animal():
    global animal
    animal='Ballena'
    #animal='Ballena'  #Varible Local -> Solo puede ser utilizada dentro del bloque donde fue creada 
    print(id(animal))

imprimir_animal()

print(animal)

#CONCLUSION
# Animal en liine 2 es un objeto diferente a animal de la linea 6.

