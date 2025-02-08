import random


def escolha_palavra():
    palavra = ["montanha", "floresta", "casa", "carro","python"]
    return random.choice(palavra)


def palavra_secreta(palavra, letras_adivinhadas):
    palavra_adivinhada = ""
    for X in palavra:
        if letras_adivinhadas == True:
         palavra +=



def jogar():
    palavra = escolha_palavra()
    tentativas = 6
    letras_adivinhadas = []

    # criar lista de letras adivinhadas
    while tentativas > 0:
        palavra_secreta(palavra,letras_adivinhadas)
        letra = input("escolhe uma letra:  ").lower()
        #verificar se a letra  já foi adivinhada
        if letra in letras_adivinhadas:
            print("letra usada tente outra")
            continue
        letras_adivinhadas.append(letra)
        if letra in palavra:
            print("boa acertaste")
        else:
            print("Errado! a letra não está na palavra ")
            tentativas -= 1
        if tentativas == 0:
            print("perdeste")
        palavra_adivinhada = True
        for letra in palavra:
            if letra not in letras_adivinhadas:
                palavra_adivinhada = False
            break

        if palavra_adivinhada:
            print("parabéns ganhaste o jogo")
            break
        else:
            print("perdeste a palavra secreta era", palavra)


jogar()
