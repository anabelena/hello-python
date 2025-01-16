#Funciones utilizadas como argumentos para otras funciones

promedio = lambda *args : sum(args)/len(args)

aprobado = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 15


def mostrar_mensaje(func_promedio, func_aprobatorio, *args): 

    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'felicidades aprobaste la materia con {promedio}.')
    else:
        print('No aprobaste la maeteria')


#mostrar_mensaje(promedio,aprobado,10,15,16,20)
mostrar_mensaje(promedio,es_aprobatorio,20,12,15,14)


