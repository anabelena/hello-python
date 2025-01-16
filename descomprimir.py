#Desempaquetado

#CREAR TUPLA
numeros=(1,2,3,4,5,6,7,8,9,10)

# * -> lista
uno,dos,tres,cuatro, *resto_numeros = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_numeros)

# *_ -> omitir valor 

uno,dos,tres,cuatro, *_ = numeros

#uno = numeros[0]
#dos = numeros[1]
#tres = numeros[2]
#cuatro = numeros[3]
#cinco= numeros[4]

print(uno)
print(dos)
print(tres)
print(cuatro)

#OMITIR elementos 

uno,dos,tres,cuatro, *_ , nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)

uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)
