agenda = {}


while True:
 nome = input("Nome (ou sair para terminar):")

 if nome.lower() == "sair":
     break


     numero = input("Número de telemóvel:")
     agenda[nome] = numero

     print("\nAgenda:")
     for nome, numero in agenda.items():
         print(f"{nome}: {numero}")



#pedir para o utilizador o nome e numero de telefone
#colocar num dicionario
#voltar a pedir para adicionar
#while True
#
#