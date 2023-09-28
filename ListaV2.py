from No import No

class ListaV2:
    CONTAGEM_ADICAO, CONTAGEM_REMOCAO = 0, 0
    def __init__(self):
        self.tamanho = 0
        self.cabeca = None
        self.final = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if self.final:
            self.final.proximo = novo_no  
            self.final = novo_no         
        else:
            self.cabeca = novo_no        
            self.final = novo_no
        self.CONTAGEM_ADICAO += 1
        self.tamanho += 1

    def remover(self, indice):
        if indice == 0:
            self.cabeca = self.cabeca.proximo
            if self.tamanho == 1:
                self.final = None  
            self.CONTAGEM_REMOCAO += 1
        else:
            atual = self.cabeca
            for _ in range(indice):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo
            if indice == self.tamanho - 1:
                self.final = atual 
        self.tamanho -= 1

    def __getitem__(self, indice):
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado if atual else None
