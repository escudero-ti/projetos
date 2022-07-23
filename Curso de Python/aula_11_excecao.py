
#tratamento de exceção
#divisão por 0
lista = [1, 10]

try:
    arquivo = open('C:/Users/escud/Documents/GitHub/projetos/Curso de Python/teste.txt', 'r')
    texto = arquivo.read()
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    divisao = a / b
    numero = lista[1]
    x = a
    print(divisao)
except ZeroDivisionError:
    print("Atenção, não é possível realizar divisão por 0.")
except IndexError:
    print("Erro ao acessar um indice inválido da lista.")
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print("Executa quando não ocorre erro.")
finally:
    print('Sempre executa.')
    print('Fechando arquivo.')
    arquivo.close()
