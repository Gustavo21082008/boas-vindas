import requests

lista = ['EUR','USD','BRL']

print('=-'*10)
de = int(input("qual a moeda de origem desejar converter? (EUR-0,USD-1,BRL-2)"))
valor = int(input())
para = int(input("qual moeda deseja converter (EUR,USD,BRL)"))
if de == 0:
    de = "EUR"
elif de == 1:
    de = "USD"
elif de == 2:
    de = "BRL"

if para == 0:
    para = "EUR"
elif para == 1:
    para = "USD"
elif para == 2:
    para = "BRL"
print()
cotacao = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(de,"-",para))
cotacao = cotacao.json()

cotacao_moeda = float(cotacao['{}'.format(de+para)]["bid"])
r = round(valor * cotacao_moeda,2)

print("O valor convertido é de ",r,para)