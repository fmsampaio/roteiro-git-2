from leitorarquivo import LeitorArquivo
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.xlabel('Valores de entrada')
    plt.ylabel('Amostragem')

    i = 1
    for serie in valores:
        plt.plot(serie, label = 'Série ' + str(i))
        i += 1
    plt.legend(loc='upper left')

    plt.show()

main()