from pympler.asizeof import asizesof

# Funções geradoras reduzem o consumo de memória da aplicação

def dobro(lista):
    for i in lista:
        yield i  # entrega ou retorna o valor

def dobro_2(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i)
    return lista_dobro

x = dobro(range(0, 10000))
y = dobro_2(range(0, 10000))

print(asizesof(x))
print(asizesof(y))


