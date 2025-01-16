#Operadores Logicos

# and, or , not

# Permiten comparar tipos booleanos. Resultado = Booleano

# AND (&&)

# Para que de True todas las condiciones deben ser TRUE
resultado_final = True and True and 10 > 5

print(resultado_final)

# OR (||)

# Para que sea verdadero por lo menos uno debe ser TRUE

resultado_final = True or False or 10 >15
print(resultado_final)

resultado_final = True and (False or 5 > 10)
print(resultado_final)

# NOT (Verdadero lo vuelve FALSE, y FALSE lo vuelve verdadero)

resultado_final = not True
print(resultado_final)

resultado_final = not False
print(resultado_final)

