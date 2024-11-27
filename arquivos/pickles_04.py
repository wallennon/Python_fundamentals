import pickle

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#instanciando a classe
p1 = Pessoas('Germano', 43)

arquivo = open('arquivo_classe.pkl', 'wb')
pickle.dump(p1, arquivo)

arquivo = open('arquivo_classe.pkl', 'rb')
retorno = pickle.load(arquivo)

print(retorno)
print(retorno.nome)
print(retorno.idade)