while True:
    entrada = int(input('Informe um número diferente de ZERO: '))

    if entrada > 0:
        print('Você digitou um número POSITIVO')
    elif entrada < 0:
        print('Você digitou um número NEGATIVO')
    elif entrada == 0:
        break
print('Programa encerrado!')