# *args é utilizando quando não sabemos a quantidade de elementos que serão passados na função
def soma_numeros(*args):
    soma = 0
    for i in args:
        soma+= i
    print(soma)

soma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)

# No **kwargs os parâmetros precisam ser nomeados
