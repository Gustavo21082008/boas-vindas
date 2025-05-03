
frase = "bla a a bla ola adeus"

palavras = frase.split()
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:contador[palavra] = 1

    print(contador)