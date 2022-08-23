from leitorarquivo import LeitorArquivo
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.xlabel('Valores de entrada')
    plt.ylabel('Amostragem')

    plt.plot(valores)
    plt.show()

main()