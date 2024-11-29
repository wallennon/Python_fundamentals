"""
A classe gato herda todos os métodos de animal
através da classe felino, que por sua vez
também herda os métodos da classe animal.
"""
class Animal:
    def andar(self):
        print("Andando da classe animal")

    def correr(self):
        print('Correndo da classe animal')

    def pular(self):
        print('pulando da classe animal')

class Felino(Animal):
    def cacar(self):
        print('Caçando da classe felino')

class Gato(Felino):
    def miar(self):
        print('Miau da classe gato')

class Cachorro(Animal):
    def latir(self):
        print('Latindo da classe cachorro')

gato = Gato()
gato.cacar()
gato.andar()
gato.miar()