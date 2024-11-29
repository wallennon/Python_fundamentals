from model import Pessoa

class PessoaDao:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.write("\n" + pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            return arq.read()
        
    
#p1 = Pessoa('Germano', 31, '98765432190')
#PessoaDao.salvar(p1) #para salvar os dados no arquivo
#print(PessoaDao.ler())