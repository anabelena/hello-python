
#Palabra reservada BREAK (permite finalizar cualquier tipo de ciclo WHILE/FOR)
titulo_curso = 'Este es mi curso'
c=0
for caracter in titulo_curso:

    if caracter == 'm':
        break  #permite finalizar de forma inmediata el CICLO

    print(caracter)
    c = c+1

print(c)

#Palabra reservada CONTINUE
#Hace que el ciclo salte a la siguiente iteracion 

micurso = 'Este es mi curso'

e=0
for curso in micurso:

    if curso == "e":
         continue 

    print(curso)



