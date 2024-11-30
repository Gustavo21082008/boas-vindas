numero_secreto = 50
adivinhou = False

i = int(input("adivinha o número que estou a pensar entre 1 e 100!"))

while not adivinhou:
    if i < numero_secreto:
        print("ok o numero escolhido está incorreto e é maior")
        i = int(input("adivinha o número que estou a pensar entre 1 e 100!"))
    if i > numero_secreto:
        print("ok o numero está incorreto e é menor")
        i = int(input("adivinha o número que estou a pensar entre 1 e 100!"))
    if i == numero_secreto:
        print("ok o numero está correto")
        adivinhou = True



