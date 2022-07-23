
#criando classe personalizada de exceção
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota ente 0 e 10: '))
        print('A nota digitada foi: {}'.format(x))
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 10.')
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')
    except InputError as ex:
        print(ex)
print('Fim do Programa!')

#o comando raise força uma exceção dentro de um try