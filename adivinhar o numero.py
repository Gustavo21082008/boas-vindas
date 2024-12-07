while True:
    print('\n 0 - Sair\n 1 - soma\n 2 - subtração\n 3 - dividir\n 4 - multiplicar ')
    escolha = int(input('qual é sua escolha?'))
    i = int(input('escolha o primeiro numero'))
    ç = int(input('escolha o segundo numero'))
    if escolha == 0:
        break
    elif escolha != 0:

     if escolha == 1:
        print("Você escoheu somar",i +ç)

    if escolha == 2:
        print("Você escolheu subtrair",i - ç)

    if escolha == 3:
        print("Você escolheu Dividir", i/ç)

    if escolha == 4:
        print("Você escolheu multiplicar", i*ç)

