# raise força uma exceção gerada pelo programador!

def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("Essa operação não pode conter números negativos!")
    return n1 + n2

print(soma(5, 4))

# Usamos o assert quando queremos definir ou forçar que algo seja verdade!
x = -5

assert x > 0, 'O valor de entrada tem que ser maior que zero!'
print(x)