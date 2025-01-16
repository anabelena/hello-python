#CONDICIONES MULTIPLES ELIF
#Se evaluan de forma descendente.
calificacion = 6

if calificacion == 10:
    print('Felicidades aprobaste con 10')
elif calificacion ==9 or calificacion ==8:
    print('Felicidades aprobaste la materia')
elif calificacion ==7 or calificacion ==6:
    print('Aprobaste la materia')
else:
    print('Reprobaste la materia')



