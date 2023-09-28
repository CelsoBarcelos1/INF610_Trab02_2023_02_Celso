from Fila import Fila 
class Dicionario:
    VERSOES_SUPORTADAS = {
        0: 'estatica',
        1: 'v1',
        2: 'v2',
        3: 'v3',
        4: 'v4'
    }

    def __init__(self, versao=0):
        versao_selecionada = self.VERSOES_SUPORTADAS.get(versao, 'estatica')
        self._chaves = Fila(versao_selecionada)
        self._valores = Fila(versao_selecionada)
        self.tamanho = 0

    def inserir(self, chave, valor):
        self._chaves.inserir(chave)
        self._valores.inserir(valor)
        self.tamanho += 1

    def remover(self):
        self._chaves.remover()
        self._valores.remover()
        self.tamanho -= 1

    def obter(self, chave):
        chave_atual = None
        valor_atual = None

        for _ in range(self.tamanho):
            chave_atual = self._chaves.remover()
            valor_atual = self._valores.remover()

            self._chaves.inserir(chave_atual)
            self._valores.inserir(valor_atual)

            if chave_atual == chave:
                return valor_atual


    def limpar(self):
        while self.tamanho != 0:
            self.remover()

    def obter_operacao_basica(self):
        return self._chaves.fila.CONTAGEM_ADICAO + self._chaves.fila.CONTAGEM_REMOCAO

    def redefinir_contadores(self):
        self._chaves.fila.CONTAGEM_ADICAO = 0
        self._chaves.fila.CONTAGEM_REMOCAO = 0
