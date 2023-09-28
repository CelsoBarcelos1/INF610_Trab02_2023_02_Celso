from numpy import empty
class ListaEstatica:
    CONTAGEM_ADICAO, CONTAGEM_REMOCAO = 0, 0
    def __init__(self, tamanho_maximo: int = 10000):
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0
        self.valores = empty(tamanho_maximo)
        
    def adicionar(self, dado):
        self.CONTAGEM_ADICAO += 1
        self.valores[self.tamanho_atual] = dado
        self.tamanho_atual += 1

    def remover(self, indice):
        for i in range(indice, self.tamanho_atual - 1):
            self.valores[i] = self.valores[i + 1]
            self.CONTAGEM_REMOCAO += 1
        self.tamanho_atual -= 1

    def __getitem__(self, indice):
        if 0 <= indice < self.tamanho_atual:
            return self.valores[indice]
