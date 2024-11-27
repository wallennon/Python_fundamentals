while True:
    sexo = input('Digite "F" para Feminino e "M" para Masculino: ')

    if sexo == "F" or sexo == "f":
        print('Você é do sexo feminino')
    elif sexo == "M" or sexo == "m":
        print('Você é do sexo masculino')
    elif sexo == '0':
            break
    else:
        print('Sexo inválido, por favor digite novamente, ou Zero para sair!')
        
print('Programa encerrado!')