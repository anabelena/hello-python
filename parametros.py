#Python los parametros pueden ser opcionales
#Valor por default siempre debe estar a la derecha
def area_circulo(radio,pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(radio=10,pi=3.14) 
#resultado= area_circulo(pi=3.14,radio=10)
#cuando trabajas con nombres de parametros no importa el orden
print(resultado)


