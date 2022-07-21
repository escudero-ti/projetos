
#importar a função date
from datetime import date, time, datetime, timedelta

# #capturando e printando a data atual do sistema
# data_atual = date.today()
# print(data_atual)
# #convertendo a exibição para o padrão brasileiro
# print(data_atual.strftime('%d/%m/%y'))
# #printando com texto
# print('Hoje é dia: {}'.format(data_atual.strftime('%d/%m/%y')))
#
# #nas diretivas do python, y minusculo traz o ano com 2 digitos e Y maiusculo traz com 4 digitos
# print('Hoje é dia: {}'.format(data_atual.strftime('%d/%m/%Y')))
#
# #imprimir o nome do dia da semana, mês e ano com 4 digitos
# data_atual_str =data_atual.strftime('%A %B %Y')
# print('Hoje é dia: {}'.format(data_atual_str))

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print('Hoje é dia: {}'.format(data_atual.strftime('%d/%m/%y')))
    print('Hoje é dia: {}'.format(data_atual.strftime('%d/%m/%Y')))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print('Hoje é dia: {}'.format(data_atual_str))

#função time permite criar um horário
def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    #convertendo para str
    # print(horario_str)
    print(horario.strftime('%H:%M:%S'))
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))

#função datetime permite acessar a data e hora atual
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    #convertendo para mostrar apenas o desejado
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    #pritando tudo, mas sem os milesegundos, basta dar um espaço entre '%d/%m/%Y e %H:%M:%S'
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))

    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.date())

    #mostrar o dia da semana em português usando tupla
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()])

    #criar uma data com datetime
    data_criada = datetime(2022, 6, 20, 15, 30, 20)
    print(data_criada)
    #converter para diretiva %c
    print(data_criada.strftime('%c'))

    #convertendo data string para datetime
    data_string = '01/01/2022'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

#realizando soma e subtração com datas e horas, exceto anos
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()



