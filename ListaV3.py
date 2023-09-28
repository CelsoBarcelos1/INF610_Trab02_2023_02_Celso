from No import No
class ListaV3:
    CONTAGEM_ADICAO, CONTAGEM_REMOCAO = 0, 0
    def __init__(self):
        self.tamanho = 0
        self.cabeca = No(None)  
        self.final = self.cabeca  

    def adicionar(self, dado):
        novo_no = No(dado)
        self.final.proximo = novo_no  
        self.final = novo_no         
        self.tamanho += 1
        self.CONTAGEM_ADICAO += 1

    def remover(self, indice):
        self.CONTAGEM_REMOCAO += 1
        atual = self.cabeca
        for _ in range(indice):  
            atual = atual.proximo
        atual.proximo = atual.proximo.proximo

        if indice == self.tamanho - 1:
            self.final = atual  
        self.tamanho -= 1

    def __getitem__(self, indice):
        atual = self.cabeca
        for _ in range(indice + 1): 
            atual = atual.proximo
        return atual.dado
