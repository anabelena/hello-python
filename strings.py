""""

lenguajes = 'Python Ruby Java Rust C++ C'

# .split(sep,maxsplit)

# Dividir cadena solo cuando aparece la primer coma maxsplit=1
listado_lenguajes = lenguajes.split() #por default si encuentra espacios
print(listado_lenguajes)


# Indicar SEPARADOR
lenguajes2 = 'Python-Ruby-Java-Rust-C++-C'
listado2 = lenguajes2.split('-',2)  #uno o mas caracteres 
print(listado2)

"""

# Metodo JOIN

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
string_lenguajes = '-'.join(lenguajes)
#string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)



