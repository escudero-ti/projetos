
#trabalhando com classes sem instanciar
#por definição, o nome das classes sempre começa com letra Maiúscula
class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def mult(self, valor_a, valor_b):
        return valor_a * valor_b

    def div(self, valor_a, valor_b):
        return valor_a / valor_b

#instanciando classes
calculadora = Calculadora()

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

#print com mensagem
print('O resultado da soma é: {}'.format(calculadora.soma(a,b)))
print('O resultado da subtração é: {}'.format(calculadora.sub(a,b)))
print('O resultado da multiplicação é: {}'.format(calculadora.mult(a,b)))
print('O resultado da divisão é: {}'.format(calculadora.div(a,b)))

#print sem mensagem
print(calculadora.soma(a,b))
print(calculadora.sub(a,b))
print(calculadora.mult(a,b))
print(calculadora.div(a,b))
