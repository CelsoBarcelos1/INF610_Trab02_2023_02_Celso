import matplotlib.pyplot as plt
import numpy as np
from Dicionario import Dicionario

n = 5 # tamanho da entrada desejado

def main():
    plt.style.use('classic')
    ob = np.zeros(n)
    length = np.arange(1, n + 1)

    for versao in range(5):
        dict_teste = Dicionario(versao)
        for alvo in range(n):
            for chave in range(alvo + 1):
                dict_teste.inserir(chave, 10)
            dict_teste.redefinir_contadores()
            dict_teste.obter(alvo)
            ob[alvo] = dict_teste.obter_operacao_basica()
            dict_teste.limpar()
            dict_teste.redefinir_contadores()
        plt.plot(length, ob)

    plt.legend(['Lista Contígua', 'Lista V1', 'Lista V2', 'Lista V3', 'Lista V4'], loc=0)
    plt.xlabel("Tamanho da Entrada (n)")
    plt.grid()
    plt.ylabel("N° vezes Op. Básica é executada [C(n)]")
    plt.tight_layout()
    plt.savefig("todas_listas.png", dpi=600)
    plt.show()

if __name__ == "__main__":
    main()