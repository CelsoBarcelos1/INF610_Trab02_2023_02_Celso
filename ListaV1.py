from No import No

class ListaV1:
    CONTAGEM_ADICAO, CONTAGEM_REMOCAO = 0, 0

    def __init__(self):
        self.tamanho = 0
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if self.cabeca:
            atual = self.cabeca
            self.CONTAGEM_ADICAO += 1
            while atual.proximo:
                atual = atual.proximo
                self.CONTAGEM_ADICAO += 1
            atual.proximo = novo_no
        else:
            self.cabeca = novo_no
            self.CONTAGEM_ADICAO += 1
        self.tamanho += 1

    def remover(self, indice):
        if indice == 0:
            self.cabeca = self.cabeca.proximo
            self.CONTAGEM_REMOCAO += 1
        else:
            atual = self.cabeca
            for _ in range(indice - 1):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo
        self.tamanho -= 1

    def __getitem__(self, indice):
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado if atual else None
