menu = '''

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> '''

saldo = 0

limite = 500
extrato = ''
num_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':

        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é invalido.')

    elif opcao == 's':
        saque = float(input("Informe o valor que deseja sacar: "))
        if saldo == 0:
            print('Você não possui saldo em conta!')
        else:
            if saque <= limite:
                if num_saques < LIMITE_SAQUES:
                    if saldo < saque:
                        print('O valor de saque é maior que o valor em conta!')
                        print(f'saldo em conta: R$ {saldo:.2f}')
                    else:
                        saldo -= saque
                        extrato += f'Saque: R$ {saque:.2f}\n'
                        num_saques += 1
                else:
                    print('Você excedeu o limite de saques diários!')
            else:
                print(
                    'O valor informado é maior que o permitido (R$ 500,00). Por favor, tente novamente!')

    elif opcao == 'e':
        print('================[EXTRATO]================')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print("Opção Inválida!")
