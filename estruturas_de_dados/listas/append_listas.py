nomes = []

while True:
    nome = input('Informe um nome ou digite -1 para sair: ')

    if nome == '-1':
        break
    
    nomes.append(nome)

print(nomes)