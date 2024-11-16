print("Qual marca de carro você quer: [0] mercedes,[1]BMW,[2],Tesla,[3] GTR")
marca_carro = int(input("escolha sua opção:"))

if marca_carro == 0:
    print("A Marca do Carro é Mercedes")
elif marca_carro == 1:
    print("A Marca do Carro é BMW")
elif marca_carro == 2:
    print("A Marca do Carro é Tesla")
elif marca_carro == 3:
    print("A Marca do Carro é GTR")

else:
    print("A Marca do Carro não existe")
