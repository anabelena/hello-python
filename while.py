# WHILE ->
# Permite ejecutar una N cantidad de veces un bloque de codigo 
# hasta que una condicion se cumpla.

#Contador del 1 a 10

contador = 1
while contador <= 10:
    print(contador)
    #contador = contador + 1
    contador += 1


numero = 123
contador_digitos=0
while numero >= 1:
    contador_digitos = contador_digitos + 1
    numero = numero / 10
    print(numero)
else:
    print('Fin de ciclo while')
    print(contador_digitos)


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  c = 0
  while c <= 20:
     print(c)
     c = c+ 1
    

    
