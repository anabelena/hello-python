#SINTAXIS ADECUADA

def make_upper(func):
    print('Entre a make_upper')
    def wrapper():
        print('llame a wrapwer')
        return func().upper()           #llamada a la funcion recibida como parametro
    
    print('voy a llamar a wrapper')
    return wrapper


@make_upper
def python_greeting():
    print('entro a python greeting')
    return 'Hi, I am a Python Developer'

#print(python_greeting())
print(python_greeting())
#variable = python_greeting()
#print(variable)