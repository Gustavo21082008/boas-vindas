stock_total = ["arroz", "feijão", "farofa"]
preço1 = [15, 14, 10]  # Corrigido para lista
quantidade = [35, 40, 100]  # Corrigido para lista
carrinho_produtos = []
carrinho_quantidade = []


def ver_stock():
    print("Estoque disponível:")
    for i in range(len(stock_total)):
        print(f"{stock_total[i]} - Preço: R${preço1[i]} - Quantidade: {quantidade[i]}")


def Comprar_Produto():
    print("Escolha um produto para comprar:")
    for i in range(len(stock_total)):
        print(f"{i + 1}. {stock_total[i]} - Preço: R${preço1[i]} - Quantidade disponível: {quantidade[i]}")

    escolha_produto = int(input("Escolha o número do produto (1, 2, 3): ")) - 1
    if escolha_produto < 0 or escolha_produto >= len(stock_total):
        print("Produto inválido!")
        return

    quantidade_comprar = int(input(f"Quantas unidades de {stock_total[escolha_produto]} você deseja comprar? "))

    if quantidade_comprar > quantidade[escolha_produto]:
        print("Quantidade indisponível no estoque!")
    else:
        carrinho_produtos.append(stock_total[escolha_produto])
        carrinho_quantidade.append(quantidade_comprar)
        quantidade[escolha_produto] -= quantidade_comprar
        print(f"{quantidade_comprar} unidades de {stock_total[escolha_produto]} foram adicionadas ao carrinho.")


def Remover_do_carrinho():
    if not carrinho_produtos:
        print("O carrinho está vazio.")
        return

    print("Produtos no carrinho:")
    for i in range(len(carrinho_produtos)):
        print(f"{i + 1}. {carrinho_produtos[i]} - Quantidade: {carrinho_quantidade[i]}")

    escolha_remover = int(input("Escolha o número do produto a remover: ")) - 1
    if escolha_remover < 0 or escolha_remover >= len(carrinho_produtos):
        print("Produto inválido!")
        return

    quantidade_remover = int(input(f"Quantas unidades de {carrinho_produtos[escolha_remover]} você deseja remover? "))
    if quantidade_remover > carrinho_quantidade[escolha_remover]:
        print("Quantidade inválida!")
    else:
        carrinho_quantidade[escolha_remover] -= quantidade_remover
        quantidade[stock_total.index(carrinho_produtos[escolha_remover])] += quantidade_remover
        if carrinho_quantidade[escolha_remover] == 0:
            carrinho_produtos.pop(escolha_remover)
            carrinho_quantidade.pop(escolha_remover)
        print(f"{quantidade_remover} unidades de {carrinho_produtos[escolha_remover]} foram removidas do carrinho.")


def Finalizar_Compra():
    if not carrinho_produtos:
        print("O carrinho está vazio. Adicione produtos para finalizar a compra.")
        return


        print("Compra não finalizada.")


def Adicionar_Estoque():
    print("Adicionar produtos ao estoque:")
    for i in range(len(stock_total)):
        print(f"{i + 1}. {stock_total[i]} - Quantidade disponível: {quantidade[i]}")

    escolha_produto = int(input("Escolha o número do produto para adicionar estoque: ")) - 1
    if escolha_produto < 0 or escolha_produto >= len(stock_total):
        print("Produto inválido!")
        return

    quantidade_adicionar = int(
        input(f"Quantas unidades de {stock_total[escolha_produto]} deseja adicionar ao estoque? "))
    quantidade[escolha_produto] += quantidade_adicionar
    print(f"{quantidade_adicionar} unidades de {stock_total[escolha_produto]} foram adicionadas ao estoque.")


while True:
    print("1. Ver estoque")
    print("2. Comprar Produto")
    print("3. Remover do Carrinho")
    print("4. Finalizar Compra")
    print("5. Adicionar Estoque")
    print("6. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        ver_stock()
    elif escolha == 2:
        Comprar_Produto()
    elif escolha == 3:
        Remover_do_carrinho()
    elif escolha == 4:
        Finalizar_Compra()
    elif escolha == 5:
        Adicionar_Estoque()
    elif escolha == 6:
        break
    else:
        print("Opção inválida!")
