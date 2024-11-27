a = int(input('numero 1: '))
b = int(input('numero 2: '))
c = int(input('numero 3: '))
maior = ''

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
    
print(f'O maior númeor é {maior}')