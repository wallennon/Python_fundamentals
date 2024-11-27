idades = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
filtro_idade = list(filter(lambda idade: idade < 18, idades))
print(filtro_idade)

dicionario = [
    {'nome':'wallennon', 'idade':25},
    {'nome':'Germano', 'idade':34},
    {'nome':'Dunga', 'idade':42}
    ]

filtro_dicionario = list(filter(lambda idade: idade['idade'] > 30, dicionario))
print(filtro_dicionario)