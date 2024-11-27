while True:
    x = input('Digite um número: ')

    if x == 'x':
        break

    try:
        num = int(x)
        print(5/num)
    except ValueError:
        print('Erro: Digite um número inteiro!')
    except ZeroDivisionError:
        print('Erro: Não é possível dividir por zero!')
    
    