#FUNCIONES QUE RECIBEN OTRA FUNCION COMO PARAMETRO
def test_function(funcionduplicar):
    numero = 20
    return funcionduplicar(numero)


def duplicate(num):
    return num * 2

print(test_function(duplicate))

