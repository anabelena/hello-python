#MODULO 3 -> TUPLAS

#Inmutables, no pueden ser modificadas.
# () Tupla

#Indices     0      1  2    3     4
tupla = ('String',10,2.6,True,[1,2,3],(4,5,6))
print(tupla)
#Tuplas son mas rapidas de leer.

cursos = ('Python','Flask','Django','Rails','MongoDB')
#            0        1        2       3       4

primercurso = cursos[2]
print(primercurso)

segundocurso = cursos[-1]
print(segundocurso)

sub_tupla = cursos[:]
print(sub_tupla)


#LISTAS Y TUPLAS

cursos = ['Python','Django','Flask']

#GENERAR TUPLA a partir de una LISTA
cursos_tupla = tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))  #Validar que tipo de variable es

niveles = ('Basico','Intermedio','Avanzado')

#GENERAR LISTA a partir de TUPLA
niveles_lista =list(niveles)
print(niveles_lista)
print(type(niveles_lista))












