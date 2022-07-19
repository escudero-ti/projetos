#
# #modulos no python são os arquivos .py que podem interagir entre eles
#
# #importar módulo via console python
# import aula_7_televisao
#
# #sempre que criarmos um módulo devemos incluir o main e identar a execução
# if __name__ == '__main__':
#
# #exemplo com o módulo televisao
#
# class Televisao:
#     def __init__(self):
#         self.ligada = False
#         self.canal = 7
#
#     def power(self):
#         if self.ligada:
#             self.ligada = False
#         else:
#             self.ligada = True
#
#     def aumenta_canal(self):
#         if self.ligada:
#             self.canal += 1
#
#     def diminui_canal(self):
#         if self.ligada:
#             self.canal -= 1
#
# if __name__ == '__main__':
#
#     #instansiar televisao
#     situacao = Televisao()
#     print('Televisão está ligada? {}'.format(situacao.ligada))#situacao atual
#     situacao.power()
#     print('Televisão está ligada? {}'.format(situacao.ligada))#situacao2
#     situacao.power()
#     print('Televisão está ligada? {}'.format(situacao.ligada))#situacao3
#     print('Canal: {}'.format(situacao.canal))
#     situacao.power()
#     print('Televisão está ligada? {}'.format(situacao.ligada))#situacao4
#     situacao.aumenta_canal()
#     situacao.aumenta_canal()
#     print('Canal: {}'.format(situacao.canal))
#     situacao.diminui_canal()
#     print('Canal> {}'.format(situacao.canal))

# #caso tenha mais de uma classe no módulo, devemos importá-lo da seguinte forma
# #impartando do módulo aula_7_televisao apenas a classe Televisao
# >>> from aula_7_televisao import Televisao
# >>> tv = Televisao()
# >>> tv.ligada
# False
# >>> tv.power()
# >>> tv.ligada
# True

#importando um módulo dentro de outro módulo
from aula_7_televisao import Televisao
from aula_7_metodos_funcoes_e_classes_calculadora1 import Calculadora

#importando um método de outro módulo
from aula_8_contador_letras import contador_letras
#é possível importar mais de um método separando-os por ,
# from aula_8_contador_letras import contador_letras, metodo2

if __name__ == '__main__':

    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    calc = Calculadora(5,10)
    print(calc.soma())

    # printando e importando um método de outro módulo
    lista = ['cachorro','gato']
    total_letras = contador_letras(lista)
    print('Quantidade de letras em cada palavra da lista: {}'.format(total_letras))

