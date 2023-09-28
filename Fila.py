from ListaEstatica import ListaEstatica
from ListaV1 import ListaV1
from ListaV2 import ListaV2
from ListaV3 import ListaV3
from ListaV4 import ListaV4

class Fila:
    VERSOES_SUPORTADAS = {
        'estatica': ListaEstatica,
        'v1': ListaV1,
        'v2': ListaV2,
        'v3': ListaV3,
        'v4': ListaV4
    }

    def __init__(self, versao='estatica', tamanho_maximo=1000):
        self.tamanho_maximo = tamanho_maximo
        self.tamanho = 0
        self.fila = self.VERSOES_SUPORTADAS[versao.lower()]()

    def inserir(self, dado):
        self.fila.adicionar(dado)
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            dado = self.fila[0]
            self.fila.remover(0)
            self.tamanho -= 1
            return dado

    def limpar(self):
        while self.tamanho != 0:
            self.remover()
