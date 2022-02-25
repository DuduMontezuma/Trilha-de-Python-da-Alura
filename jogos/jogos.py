import forca
import adivinhacao

def escolhe_jogo():
    print('*' * 32)
    print('ESCOLHA O SEU JOGO')
    print('*' * 32)

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual é o jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()