while True:
    USUARIO = 'wall'
    SENHA = "senha123"

    user = input('Usuário: ')
    if user == '0':
        print("Programa Encerrado!")
        break
    passworld = input('Senha: ')

    
    if user == USUARIO and passworld == SENHA:
        print('Acesso permitido')
    else:
        print('Usuário e Senha incorretos, tente novamente')