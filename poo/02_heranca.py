"""
o self - faz referencia à instância
o cls - faz referencia à classe
o super - faz referência à classe "pai" que está sendo herdada
"""
class Pessoa:
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Estou falando como pessoa')
    
class Vendedor(Pessoa):
    def vender(self):
        print('Estou vendendo')
    
class Cliente(Pessoa):
    def comprar(self):
        print('Estou comprando')

    #sobreposição de métodos
    def falar(self):
        #primeiro irá imprimir o método da classe pai, depois o método da classe.
        super().falar()
        print('Estou falando como cliente')

#criando instâncias das classes
c1 = Cliente()
v1 = Vendedor()

#chamando os métodos
print('Cliente:')
c1.andar()
c1.falar()
c1.comprar()
print('- ' * 10)
print('Vendedor:')
v1.vender()
v1.falar()
v1.andar()
