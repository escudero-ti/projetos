
#criando listas - use []
# lista_numero = [1, 3, 5, 7]
# lista_animal = ['cachorro','gato','elefante']
# print(lista_numero)
# print(lista_animal)

#imprimindo uma posição específica da lista
#as listas começam sempre na posição 0
# print(lista_numero[0])
# print(lista_animal[1])

# #fazendo soma de inteiros na lista_numero
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro','gato','elefante']
# print(lista_animal[1])
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

#fazendo soma de inteiros na lista de forma reduzida
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro','gato','elefante']

# #soma
# print(sum(lista))
#
# #maior valor
# print(max(lista))
#
# #menor valor
# print( min(lista))

# #verificar a existencia de um valor na lista
# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro','gato','elefante']
#
# a = int(input('Digite um número: '))
#
# if a in lista:
#     print('O valor digitado foi: {} e está na lista!'.format(a))
# else:
#     print('Valor digitado não está na lista!')

#verificar a existencia de um valor na lista com laço while
# lista = [1, 3, 5, 7]
#
# a = int(input('Digite um número: '))
#
# while a not in lista:
#     print('Valor digitado não está na lista!')
#     a = int(input('Digite outro número: '))
# else:
#     print('O valor digitado foi: {} e está na lista!'.format(a))

# #repetir dados da lista
# lista = [1,3,5,7]
# x = lista * 3
# print(x)

#verificar se um nome está na lista e se não estiver incluir
lista_nome = ['eduardo','carol']

nome = input('Digite seu primeiro nome: ')

if nome in lista_nome:
    print('O nome digitado foi {} e já está na lista! '.format(nome))
    print(lista_nome)
else:
    print('O nome digitado foi: {} e não estava na lista, sendo assim, acabamos de incluí-lo! '.format(nome))
    lista_nome.append(nome)
    print(lista_nome)
#append - inclui um dado na lista
# pop - exclui um dado de uma posição específica na lista_nome
# remove - exclui o dado com base no valor informado

#criando tuplas - use ()
#não é possível alterar os dados de uma posição na tupla
# num = (1,4,5,8,10)
# print(num)

#contando quantos registros há em uma tupla ou lista
# print(len(num))

# #convertendo lista para tupla
# nome = ['eduardo','carol','juan','alicia']
# print(nome)
#
# tupla_nome = tuple(nome)
# print(tupla_nome)

# #convertendo tupla para lista
# tupla_num = (1,3,5,7,9)
# print(tupla_num)
# lista_num = list(tupla_num)
# print(type(lista_num))
# print(lista_num)