pessoas = []
while True:
    decisao = int(input('Digite 1 para CADASTRAR e 0 (zero) para SAIR: '))
    if decisao == 0:
        break

    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ')
    pessoa = {'nome': nome, 'idade': idade, 'sexo': sexo}
    pessoas.append(pessoa)

    """
    Também pode ser feito das seguintes formas:
    Passando o dicionário através da variável 'pessoa', realizando o append() da variável
    pessoa = {'nome': input('Digite o nome: '), 'idade': int(input('Digite a idade: ')), 'sexo': input('Digite o sexo (M/F): ')}
    pessoas.append(pessoa)

    OU passando diretamente dentro do append de pessoas:

    pessoas.append({'nome': input('Digite o nome: '), 'idade': int(input('Digite a idade: ')), 'sexo': input('Digite o sexo (M/F): ')})
    """


for pessoa in pessoas:
    print(pessoa)
