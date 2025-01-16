lista_cursos=['Python','Django','Flask','Ruby','Java','Rust']
print(lista_cursos)

#Para trabajar con SUBLISTAS necesitamos INDICE INICIAL Y FINAL

#[start:end] -> obtenemos una sublista a partir de un rango
#[start:] -> obtenemos los ultimos elementos de la lista
#[:start] -> obtenemos los primeros elementos de la lista
#[start:end:skip] -> saltos 

#Sublistas
sub_lista=lista_cursos[1:4]
print(sub_lista)

#Ultimos elementos de la lista
sub_lista=lista_cursos[1:]
print(sub_lista)

#Primeros elementos de la lista
sub_lista=lista_cursos[:3]
print(sub_lista)


#Generar LISTA con SALTOS
sub_lista=lista_cursos[1:5:2]
print(sub_lista)
