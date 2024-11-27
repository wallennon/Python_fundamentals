x = [i for i in range(12, 26)]
x = list(map(lambda x: "é nenor" if x < 18 else(x), x))
print(x)

pessoa = [{'nome': 'wallennon', 'idade': 34, 'inss':'Contribuinte do INSS'}, {'nome': 'Raimundo', 'idade': 66, 'inss':'Contribuinte Ativo'}]

pessoa = list(map(lambda pessoa: {'nome': pessoa['nome'], 'idade': pessoa['idade'], 'inss': 'Aposentado'} if pessoa['idade'] > 65 else(pessoa), pessoa))
print(pessoa)