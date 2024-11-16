print("Qual é seu ordenado:")
ordenado = int(input())

if ordenado < 500:
    reajuste=ordenado*0.15+ordenado
    print("O seu ordenado será",reajuste)
if ordenado >= 500 and ordenado <= 1000:
    reajuste=ordenado*0.10+ordenado
    print("O seu Ordenado será",reajuste)
if ordenado>1000:
    reajuste = ordenado*0.5+ordenado
    print("O seu ordenado será",reajuste)