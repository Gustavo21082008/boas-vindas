with open("ficheiro.txt", "r", encoding="utf-8")as file1:
    conteudo = file1.readlines()
    print(conteudo)
    for linha in conteudo:
        print(linha)

with open("ficheiro.tlt","w")as file2:
    conteudo2 = file2.write("das")
    print(conteudo2)