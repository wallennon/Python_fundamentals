x = lambda: 10
print(x())

y = lambda : print('wallennon')
y()

def teste():
    return lambda *idade : print(idade)

age = teste()
age(34)