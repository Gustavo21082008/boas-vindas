with open("ficheiro.txt","w",encoding="utf-8")as file2:
    file2.write("João\nAlice\nDiogo\nFrancisco\nMaria")
def escrever():
   with open("ficheiro.txt","r",encoding="utf-8")as file2:
         conteudo2 = file2.readlines()
         for linha2 in conteudo2:
            print(linha2)

escrever()

def contar():
    with open("ficheiro.txt","r",encoding="utf-8")as file2:
        soma = 0
        conteudo2 = file2.readlines()
    #conteudo = ["João","Francisco","Alice","Diogo","Ana","Maria"
        for i in conteudo2:
            soma += 1

        print(soma)

contar()