# No **kwargs os parâmetros precisam ser nomeados
def soma_numeros(**kwargs):
    print(kwargs['teste1'])
    x = kwargs.get('teste4')
    if x:
        print('Foi passado')
    else:
        print('Não foi passado')

soma_numeros(teste1 = "Aprendendo", teste2 = 2, teste3 = 3)

