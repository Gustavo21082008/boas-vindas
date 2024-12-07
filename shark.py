
soma = 0
frase = input('Qual é a frase')
letra = input('Qual é a letra que deseja procurar')

for i in frase:
    if i== letra:
        soma += 1
print(f'esta frase tem {soma} letras {letra}')


