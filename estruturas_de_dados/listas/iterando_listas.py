idades = [9, 15, 2, 8 , 33, 51, 0 , 29]

# for i in (range(0, len(idades))):
#     print(f'Indice: {i} e idade {idades[i]}')
# soma = 0
# for idade in idades:
#     print(f'Idade: {idade}')
#     soma += idade

# print('A soma das idades é: ', soma)

idades_pares = []

for idade in idades:
    if idade > 0 and idade % 2 == 0:
        idades_pares.append(idade)

print(idades_pares)