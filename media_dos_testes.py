nota_do_teste1 = int(input("Qual é a nota do teste1?"))
nota_do_teste2 = int(input("Qual é a nota do teste2?"))
media_dos_testes = (nota_do_teste1+nota_do_teste2)/2
if media_dos_testes <50:
    print("aluno reprovado")

if media_dos_testes >=50:
    print("aluno aprovado")