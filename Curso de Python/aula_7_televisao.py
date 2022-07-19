
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 7

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':

    #instansiar televisao
    situacao = Televisao()
    print('Televisão está ligada? {}'.format(situacao.ligada))#situacao atual
    situacao.power()
    print('Televisão está ligada? {}'.format(situacao.ligada))#situacao2
    situacao.power()
    print('Televisão está ligada? {}'.format(situacao.ligada))#situacao3
    print('Canal: {}'.format(situacao.canal))
    situacao.power()
    print('Televisão está ligada? {}'.format(situacao.ligada))#situacao4
    situacao.aumenta_canal()
    situacao.aumenta_canal()
    print('Canal: {}'.format(situacao.canal))
    situacao.diminui_canal()
    print('Canal> {}'.format(situacao.canal))
