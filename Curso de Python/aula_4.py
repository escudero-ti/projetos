#uso do for e range
#contagem de números
# for x in range(100):
#     print(x)

#a partir do 1 ou qualquer valor
# for x in range(1,100):
#     print(x)

# #verificar se um número digitado é primo
# a = int(input('Digite um número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x,resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))

#mostrar apenas os números primos até o número digitado pelo user utilizando 2 for
# a = int(input('Difite um número: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

#uso do while
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

#validar notas recebidas
a = int(input('Informe a Primeira Nota: '))
while a > 10:
    a = int(input('Você digitou a primeira nota errada! Digite novamente: '))
b = int(input('Informe a Segunda Nota: '))
while b > 10:
    b = int(input('Você digitou a segunda nota errada! Digite novamente: '))
c = int(input('Informe a Terceira Nota: '))
while c > 10:
    d = int(input('Você digitou a segunda nota errada! Digite novamente: '))
d = int(input('Informe a Quarta Nota: '))
while d > 10:
    d = int(input('Você digitou a segunda nota errada! Digite novamente: '))
media = (a + b + c + d) / 4
print('\nMedia igual à: {}'.format(media))

if media >= 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
