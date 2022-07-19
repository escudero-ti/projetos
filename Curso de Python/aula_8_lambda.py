
# #lambda é uma função anonima, ou seja, uma forma de simplicar algo ue será utilizado mais de uma vez no código
# contador_letras = lambda lista: [len(x) for x in lista]
#
# lista_animais = ['cachorro', 'gato', 'passaro']
# print(contador_letras(lista_animais))
#
# #lambda é eficiente para coisas que da pra resolver em uma linha

# #calculadora com lambda
# soma = lambda a, b: a + b
# subtracao = lambda a, b: a - b
# multiplicacao = lambda a, b: a * b
# divisao = lambda a, b: a / b
#
# print(soma(10,5))
# print(subtracao(10,5))
# print(multiplicacao(10,5))
# print(divisao(10,5))

#calculadora com lambda e dicionário de funções

#dicionário de funções
calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,

}

soma = calculadora['soma']
subtracao = calculadora['sub']
multiplicacao = calculadora['mult']
divisao = calculadora['div']
print('O resultado da soma é: {}'.format(soma(10,5)))
print('O resultado da subtracao é: {}'.format(subtracao(10,5)))
print('O resultado da multiplicação é: {}'.format(multiplicacao(10,5)))
print('O resultado da divisão é: {}'.format(divisao(10,5)))
