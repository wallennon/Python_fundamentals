# import minha_lib // aqui está importando tudo que está dentro do arquivo
from minha_lib import x as x_lib
from minha_lib import soma_numero
from funcoes.minhas_funcoes import tabuada #puxando arquivo de outra pasta
x = 50

print(x)
print("--------")
print(x_lib) 

soma = soma_numero(10, 5)
print(f'Retorno da função: {soma}')

print('Imprimindo a tabuada:')
tabuada = tabuada(3)
