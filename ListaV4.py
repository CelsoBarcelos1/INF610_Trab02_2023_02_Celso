from NoDuplo import NoDuplo
class ListaV4:
    CONTAGEM_ADICAO, CONTAGEM_REMOCAO = 0, 0

    def __init__(self):
        self.tamanho = 0
        self.cabeca = NoDuplo(None)  
        self.final = self.cabeca

    def adicionar(self, dado):
        novo_no = NoDuplo(dado)
        novo_no.anterior = self.final
        self.final.proximo = novo_no  
        self.final = novo_no        
        self.tamanho += 1
        self.CONTAGEM_ADICAO += 1

    def remover(self, indice):
        self.CONTAGEM_REMOCAO += 1
        atual = self.cabeca
        for _ in range(indice + 1):  
            atual = atual.proximo

        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo  

        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.final = atual.anterior
        self.tamanho -= 1

    def __getitem__(self, indice):
        atual = self.cabeca
        for _ in range(indice + 1): 
            atual = atual.proximo
        return atual.dado
