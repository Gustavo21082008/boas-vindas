print ("qual moeda quer converter: [0] Dolar, [1] Real")
moeda = int(input("escolha sua opção:"))
euros = float(input("quantos euros deseja converter:"))

dolar = euros * 1.08
real = euros * 6.17

if moeda == 0:
    print("Vai ficar com",dolar,"dolares.")

if moeda == 1:
    print("Vai ficar com",real,"reais")