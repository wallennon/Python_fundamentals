import pickle

class Pessoa:
    nome = 'wallennon'
    idade = 34


arquivo = open('arquivo_da_classe.pkl', 'wb')
pickle.dump(Pessoa, arquivo)

arquivo = open('arquivo_da_classe.pkl', 'rb')
retorno = pickle.load(arquivo)

print(retorno)
print(retorno.nome)
print(retorno.idade)