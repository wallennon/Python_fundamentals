#realizando serialização de arquivo
import pickle

x = [1,2,3,4]

arquivo = open('arquivo.pkl', 'wb')
pickle.dump(x, arquivo)
print(arquivo)

arquivo = open('arquivo.pkl', 'rb')
data = pickle.load(arquivo)

print(data)
