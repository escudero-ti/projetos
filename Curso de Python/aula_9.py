
#utilizando builtins
#criando arquivo teste - w = write/escrever
# open('teste.txt', 'w')
#
# #escrevendo no arquivo
# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita')
# arquivo.close()

# #obs.: o camando w do open subscreve o que está escrito no arquivo, para acrescentar um texte ao arquivo existente sem apagar o texto anterior utiliza-se o a.
# #escrevendo no arquivo
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nAcrescentando texto ao arquivo.')
# arquivo.close()

#importando bibliotecas python
import shutil

#definição de métodos
def criar_arquivo_local(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def criar_arquivo_dir(nome_arquivo, texto):
    diretorio = 'C:/Users/escud/PycharmProjects/pythonProject/Teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo_local(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo_dir(texto):
    diretorio = 'C:/Users/escud/PycharmProjects/pythonProject/Teste.txt'
    arquivo = open(diretorio, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') #um split converte o conteúdo do arquivo para uma lista com base no atributo dentro de split

    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')#quebra pela virgula
        aluno = lista_notas[0]
        lista_notas.pop(0)#separar a string (nome) dos inteiros (notas)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#importando bibliotécas do python dentro de um método
#criando um método para copiar arquivos para outro diretório
def copia_arquivos(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/escud/Documents/GitHub/projetos/Curso de Python/')

#método para mover arquivo
def move_arquivos(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/escud/Downloads')


#utilização de métodos
if __name__ == '__main__':
    move_arquivos('Teste.txt')

    #copia_arquivos('Teste.txt')

    # lista_media = media_notas('Notas.txt')
    # print(lista_media)

    # #utilizando o método criar_arquivo_local
    # criar_arquivo_local('Primeira linha. \n')
    # #utilizando o método criar_arquivo_dir
    # criar_arquivo_dir('Primeira linha. \n')

    #utilizando o método atualizar_arquivo
    # aluno = 'Eduardo, 10, 10, 5, 5\n'
    # atualizar_arquivo_local('Notas.txt', aluno)
    #ler_arquivo('teste.txt')
    #atualizar_arquivo_dir('Acrescentando texto.\n')
    # ler_arquivo('teste.txt')

