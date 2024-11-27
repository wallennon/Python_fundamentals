class Pessoas():
    # criando atributos de classe
    possui_olho = True
    possui_boca = True
    raca = 'Ser humano'

    # criando métodos de classe
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    # usando função recursiva
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logado no sistema!')
        # se não fosse função recursiva, poderia passar o self.nome direto
        # sem necessitar da função retorna_nome

    @classmethod
    def andar(cls):
        print('Estou andando')

p1 = Pessoas('Wallennon', 34, '081334')
p2 = Pessoas('Germano', 41, '482429')

p1.logar_sistema()
p2.logar_sistema()
p1.andar()

Pessoas.andar()