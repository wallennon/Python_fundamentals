n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

try:
    print(int(n1/n2))
except:
    print('Não Deu! ;/')
finally: # sempre será executado <<<
    print('Fim do programa!')