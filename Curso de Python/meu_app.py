#meu app
#input do usuário e conversão de str para int
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#conversao utilizando o format
# print('Soma: {}'. format(soma))
# print('Subtracao: {}'. format(subtracao))
# print('Multiplicacao: {}'. format(multiplicacao))
# print('Divisao: {}'. format(divisao))
# print('Resto: {}'. format(resto))

#conversao em uma linha só
#print('Soma: {} Subtracao: {} Multiplicao: {} Divisao: {} Resto: {}'. format(soma,subtracao,multiplicacao,divisao,resto))

#conversao em uma linha só e pulando linha = identado
print('\nSoma: {soma} '
      '\nSubtracao: {sub} '
      '\nMultiplicao: {mult} '
      '\nDivisao: {div} '
      '\nResto: {resto}'.format(soma=soma,
                                sub=subtracao,
                                mult=multiplicacao,
                                div=divisao,
                                resto=resto))