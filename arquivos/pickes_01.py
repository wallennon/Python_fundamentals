import pickle

x = [1,2,3,4]
lista = {'nome':'wallennon', 'idade':34, 'cidade': 'João Pessoa'}

string = pickle.dumps(x)
descricao = pickle.dumps(lista)

print(string)
print(pickle.loads(string))
print(type(pickle.loads(string)))

print('-'*50)

print(descricao)
print(pickle.loads(descricao))
print(pickle.loads(descricao)['cidade'])
print(type(pickle.loads(descricao)))
