# w para escrita - a para adicionar|(append) - r para leitura 

with open('pessoas.txt', 'r') as arquivo:
# while True:
#     nome = input('Digite o nome da pessoa: ')
#     idade = input('Informe a idade: ')

#     if nome == '0':
#         break

#     arquivo.write(f'{nome} {idade}\n')

    resultado = arquivo
    pessoas = []

    for pessoa in resultado:
        pessoas.append(pessoa.split())

    print(pessoas)