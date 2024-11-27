pessoa = {
    'nome' : 'Wallennon Germano',
    'idade' : 25,
    'cidade' : 'São Paulo',
    'estado' : 'SP',
    'profissao' : 'Desenvolvedor'
}

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print("--------------------------------")

for i, j in pessoa.items():
    print(f'Chave: {i}, Valor: {j}')
