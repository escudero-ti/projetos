#validação de 2 valores
# a = int(input('Informe o primero valor: '))
# b = int(input('Informe o segundo valor: '))
#
# #if e else
# if a > b:
#     print('\nO maior valor digitado foi: {}'.format(a))
# else:
#     print('\nO maior valor digitado foi: {}'.format(b))
# print('\nFim do programa!')

#validação de 3 ou mais valores
# a = int(input('Informe o primero valor: '))
# b = int(input('Informe o segundo valor: '))
# c = int(input('Informe o terceiro valor: '))
#
#if e else
# if a > b and a > c:
#     print('\nO maior valor digitado foi: {}'.format(a))
# elif b > a and b > c:
#     print('\nO maior valor digitado foi: {}'.format(b))
# else:
#     print('\nO maior valor digitado foi: {}'.format(c))
# print('\nFim do programa!')

#validar par ou impar com operador lógico == (igual)
# a = int(input('Digite um número: '))
# resto = a % 2
# if resto == 0:
#     print('O número é par!')
# else:
#     print('O número é impar!')

#validar par ou impar entre 2 valores digitados com or e not
# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
# #if resto_a == 0 or not resto_b > 0:
#     print('Um número par foi digitado!')
# else:
#     print('Nenhum número par foi digitado!')

#validar notas recebidas
a = int(input('Primeira nota: '))
if a > 10:
    a = int(input('Você digitou a primeira nota errada! Digite novamente: '))
b = int(input('Segunda nota: '))
if b > 10:
    b = int(input('Você digitou a segunda nota errada! Digite novamente: '))
c = int(input('Terceira nota: '))
d = int(input('Quarta nota: '))
media = (a + b + c + d) / 4
print('\nMedia igual à: {}'.format(media))

if media >= 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
