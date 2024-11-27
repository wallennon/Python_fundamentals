nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
nota_3 = float(input('Informe a terceira nota: '))
nota_4 = float(input('Informe a quarta nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(media)

if media >= 6:
    print('Aprovado')
elif media >= 4:
    print('Recuperação')
else:
    print('Reprovado')