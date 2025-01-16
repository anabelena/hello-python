#DECORADORES -> SINTAXIS POCO UTILIZADA, NO RECOMENDADA.

def make_upper(func):

    def wrapper():

        return func().upper()
    
    return wrapper



def python_greeting():

    return 'Hola, Soy un Python developer'


python_greeting = make_upper(python_greeting)  #This is what decorates the function
print(python_greeting())



