import random

def escolha_palavra():
    palavra=["montanha","floresta","casa","carro"]
    return random.choice(palavra)

def jogar():
    palavra = escolha_palavra()
    print(palavra)
    tentativas = 6
    letras_adivinhadas = []
    # criar lista de letras adivinhadas
    while tentativas>0:
        letra = input("escolhe uma letra:  ").lower()
        #verificar se a letra  já foi adivinhada
        if letra in letras_adivinhadas:
            print("letra usada tente outa")
            continue
        letras_adivinhadas.append(letra)
        if letra in palavra:
            print("boa acertaste")
        else:
            print("Errado! a letra não está na palavra ")
            tentativas -= 1
        if tentativas == 0:
            print("perdeste")
        palavras_adivinhada = True
        for i in palavra:

jogar()
