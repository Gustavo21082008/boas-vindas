with open("ficheiro.txt","w",encoding="utf-8")as file2:
    file2.write("João\nAlice\nDiogo\nFrancisco\nMaria\nAna")
def escrever():
   with open("ficheiro.txt","r",encoding="utf-8")as file2:
         conteudo2 = file2.readlines()
         for linha2 in conteudo2:
            print(linha2)

#escrever()
def contar():
    with open("ficheiro.txt","r",encoding="utf-8")as file2:
        soma = 0
        conteudo2 = file2.readlines()
    #conteudo = ["João","Francisco","Alice","Diogo","Ana","Maria"
        for i in conteudo2:
            soma += 1

        print(soma)


#contar()

def criar_ficheiro():
    nome_ficheiro = input("qual será o nome do seu Ficheiro?")
    nome_completo = f"{nome_ficheiro}.txt"
    with open(nome_completo,"w")as file3:
     pass

    print(f"O,{nome_ficheiro} foi criado")

def inserir_frase():
    #pedir nome do ficheiro ao utilizador
    #pedir qual é a frase que ele quer escrever no ficheiro
    #abrir o ficheiro e escrever a frase lá dentro
    #dar print de uma mensagem a dizer que a frase foi escrita com sucesso

    nome_ficheiro = input("Qual o nome do ficheiro:")
    nome_completo = f"{nome_ficheiro}.txt"
    with open(nome_completo,"a") as ficheiro:
        frase = input("Digite a frase que deseja inserir: ")
        ficheiro.write(frase + "\n")
        print(f"frase adicionada ao ficheiro {nome_completo} com sucesso!")
1
def ler_ficheiro():
    nome_ficheiro = input("qual o nome do seu Ficheiro?: ")
    nome_completo = f"{nome_ficheiro}.txt"
    with open(nome_completo,"r")as ficheiro:
        conteudo = ficheiro.read()
        if conteudo:
            print("\nConteudo do ficheiro:")
            print(conteudo)
        else:
            print(f"ficheiro{nome_completo} está vazio.")


def menu():
    while True:
        print("\n Menu: ")
        print(" 1. criar ficheiro")
        print(" 2. inserir frase num ficheiro")
        print(" 3. ler o conteudo do ficheiro")
        print(" 4. Sair")
        escolha = int(input("escolha uma opção"))

        if escolha == 1:
            criar_ficheiro()
        elif escolha == 2:
            inserir_frase()
        elif escolha == 3:
            ler_ficheiro()
        elif escolha == 4:
            break
        else:
            print("Opção invalidá")

menu()