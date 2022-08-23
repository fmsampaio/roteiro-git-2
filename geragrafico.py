from leitorarquivo import LeitorArquivo
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.xlabel('Valores de entrada')
    plt.ylabel('Amostragem')

    for serie in valores:
        plt.plot(serie)
        
    plt.show()

main()