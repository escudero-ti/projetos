#
# #metodo é definido com dif
# #metodo possibilita o reaproveitamento de código
# def soma(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mult(a,b):
#     return a*b
#
# def div(a,b):
#     return a/b
#
# # print(soma(1, 2))
# # print(soma(3, 4))
#
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
#
# print('O resultado da soma é: {}'.format(soma(a,b)))
# print('O resultado da subtração é: {}'.format(sub(a,b)))
# print('O resultado da multiplicação é: {}'.format(mult(a,b)))
# print('O resultado da divisão é: {}'.format(div(a,b)))

#trabalhando com classes
#por definição, o nome das classes sempre começa com letra Maiúscula
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

#instanciando classes
calculadora = Calculadora(10,2)

#print com mensagem
print('O resultado da soma é: {}'.format(calculadora.soma()))
print('O resultado da subtração é: {}'.format(calculadora.sub()))
print('O resultado da multiplicação é: {}'.format(calculadora.mult()))
print('O resultado da divisão é: {}'.format(calculadora.div()))

#print sem mensagem
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.div())
