
#use [] para criar listas
#use () para criar tuplas
#use {} para criar conjuntos

# #criando conjuntos e trabalhando com funções
# conjunto = {1,2,3,4,5}
# print(conjunto)
# #um conjunto somente mostra um item de cada, mesmo que ele esteja repetido
#
# #add elementos em um conjunto
# conjunto.add(6)
# print(conjunto)
# #será impresso o conjunto com o valor 5 add
#
# #remover elementos em um conjunto
# conjunto.discard(6)
# print(conjunto)
# #será removido o celemento 2 do conjunto

# #união de conjuntos
# conjunto1 = {1,2,3,4,5}
# conjunto2 = {5,6,7,8,9}
# conjunto_uniao = conjunto1.union(conjunto2)
# print('União: {}'.format(conjunto_uniao))
#
# #interseccao de conjuntos = imprime apenas os iguais
# conjunto_interseccao = conjunto1.intersection(conjunto2)
# print('Intersecção: {}'.format(conjunto_interseccao))
#
# #diferença de conjuntos = imprime os diferentes de acordo com a ordem informada
# conjunto_diferenca = conjunto1.difference(conjunto2) #imprime os elementos do conjunto1 que não estão no conjunto2
# print('Diderença entre 1 e 2: {}'.format(conjunto_diferenca))
# conjunto_diferenca = conjunto2.difference(conjunto1) #imprime os elementos do conjunto2 que não estão no conjunto1
# print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca))
# conjunto_dif_simetrica = conjunto1.symmetric_difference(conjunto2)
# print('Diferença Simétrica entre 1 e 2: {}'.format(conjunto_dif_simetrica))#imprime todos exceto os iguais

# conjunto_a = {1,2,3}
# conjunto_b = {1,2,3,4,5}
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# conjunto_subsetb = conjunto_b.issubset(conjunto_a)
# print('conjuntoa é um subconjunto de conjuntob: {}'.format(conjunto_subset))
# print('conjuntob é um subconjunto de conjuntoa: {}'.format(conjunto_subsetb))
#
# #superconjunto é o contrário de subconjunto
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('conjuntob é um superconjunto de conjunto a: {}'.format(conjunto_superset))

#converter lista para conjunto para tirar duplicidade
lista = ['cachorro', 'cachorro', 'gato', 'gato','elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
