#trabalhando com pacotes

# comandos
# pip __version = informa a versão instalada do pip
# pip --help = mostra o manual do pip
#
# instalar pacote requests para fazer chamada de url
# pip install requests

#importando requests
import requests

# response = requests.get('https://viacep.com.br/ws/01001000/json/')
# #200 = existe e 400 = não existe
# print(response.status_code)
# #imprime todo o conteúdo coletado da url
# print(response.text)
#
# #converter os dados capturados para um dicionário para permitir acessar uma informação expecífica
# print(response.json())
#
# #guardar os dados e depois consultar apenas o desejado
# dados_cep = response.json()
# print(dados_cep['logradouro'])
# print(dados_cep['cep'])
# print(dados_cep['uf'])

#criando um método para importar dados do cep
def retorna_dados_cep(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['cep'])
    print(dados_cep['uf'])

#módulo para raspagem de dados de sites
def retorna_response(url):
    response = requests.get(url)
    return response.text

#chamando e executando métodos
if __name__ == '__main__':
    #retorna_dados_cep(input('Digite o CEP desejado: '))
    #response = retorna_response('https://www.corinthians.com.br/')
    response = retorna_response(input('Digite a URL desejada: '))
    print(response)
