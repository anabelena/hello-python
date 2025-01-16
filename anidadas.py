def operacion(cantidad,balance,tipo='deposito'):
    #Primera funcion
    def deposito(cantidad,balance):

        return cantidad+balance
    
    #Segunda funcion
    def retiro(cantidad,balance):
        if cantidad <=balance:
            return balance-cantidad
        else:
            return None
        

    if tipo == 'deposito':
        return deposito(cantidad,balance)
    elif tipo == 'retiro':
        return retiro(cantidad,balance)
    


resultado = operacion(10,50)
print(resultado)
    
