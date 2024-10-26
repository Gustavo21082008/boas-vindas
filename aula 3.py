print("insira os dados do item 1")
item1 = input("Qual é o nome do item 1:")
preço1 = float(input("preço do item1 em euros:"))
Quantidade1 = int(input("Quantidade do item 1:"))

print("insira os dados do item 2")
item2 = input("Qual é o nome do item 2:")
preço2 = float(input("preço do item2 em euros:"))
Quantidade2 = int(input("Quantidade do item 2:"))


print("insira os dados do item 3")
item3 = input("Qual é o nome do item 3:")
preço3 = float(input("preço do item 3 em euros:"))
Quantidade3 = int(input("Quantidade do item 3:"))

valor_stock_1 = preço1 * Quantidade1
valor_stock_2 = preço2 * Quantidade2
valor_stock_3 = preço3 * Quantidade3

valor_total_stock = valor_stock_1 + valor_stock_2 + valor_stock_3

print("Resumo do stock:")

print("item1:",item1,"|preço1:",str(preço1),"|quantidade:",str(Quantidade1),"|valor do stock1",valor_stock_1)
print("item2",item2,"|preço2:",str(preço2),"Quantidade2:",str(Quantidade2),"|valor do stock2",valor_stock_2)
print("item3",item3,"|preço3:",str(preço3),"Quantidade3:",str(Quantidade3),"|valor do stock3", valor_stock_3)
print("O valor total do stock é",valor_total_stock)