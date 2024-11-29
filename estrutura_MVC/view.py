from controller import PessoaController

while True:
    decisao = int(input(' Digite 1 para salvar uma pessoa:\n Digite 2 para ver as pessoas salvas em uma lista:\n Digite 0 para sair: '))
    
    if decisao == 0:
        break
    elif decisao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite seu CPF (apenas números): ')

        if PessoaController.cadastrar(nome, idade, cpf):
            print('Pessoa cadastrada com sucesso!')
        else:
            print('Valores inválidos! Tente novamente.')
    
    elif decisao == 2:
        print('Pessoas salvas: ')