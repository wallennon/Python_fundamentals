import textwrap
# formata parágrafos de texto para que caibam em uma dada largura de tela

# função para mostrar o menu do sistema


def menu():
    menu = """\n
    =============== MENU ===============
    [d]\t Depositar
    [s]\t Sacar 
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t R${valor:.2f}\n'
        print("\n>>> Depósito realizado com sucesso! <<<")
    else:
        print("\nXXX Operação falhou! Valor informado é inválido. XXX")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nXXX Operação falhou! Saldo insuficiente. XXX")
    elif excedeu_limite:
        print("\nXXX Operação falhou! Limite insuficiente. XXX")
    elif excedeu_saques:
        print("\nXXX Operação falhou! Número máximo de saques excedido. XXX")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t R${valor:.2f}\n'
        numero_saques += 1
        print("\n >>> Saque realizado com sucesso! <<<")

    else:
        print("\nXXX Operação falhou! Valor informado é inválido. XXX")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== Extrato ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo:\t R${saldo:.2f}')
    print('======================================')


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nXXX Já existe usuário com este CPF! XXX")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro , numero - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })

    print("===== Usuário criado com sucesso! =====")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n >>> Conta criada com Sucesso! <<<")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }

    print("\n XXX Usuário não encontrado, fluxo de criação de conta encerrado! XXX")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência:\t {conta['agencia']}
            C/C:\t {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do Depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print("Opção Inválida!")


main()
