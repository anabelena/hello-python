def saludar(username):
    mensaje = f'Hola {username}' #mensaje: variable local

    def mostrar_mensaje():   #anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)
respuesta()

