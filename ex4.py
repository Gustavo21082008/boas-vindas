numero = int(input("escolha um numero"))

print("os numerosque antecedem esse numero são:")

for i in range (1,numero + 1,1):
    if i % 2 == 0:
     print (i)