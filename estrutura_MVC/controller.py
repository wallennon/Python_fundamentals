from dao import PessoaDao
from model import Pessoa

class PessoaController:
    @classmethod
    def cadastrar(cls, nome: str, idade: int, cpf: str):

        if len(nome) > 2 and (idade > 0 and idade <125) and len(cpf) == 11:
            try:
                PessoaDao.salvar(Pessoa(nome, idade, cpf))
                return True
            except:
                return False
        else:
            return False
        
#PessoaController.cadastrar("Vaqueiro", 61, '15975312378')
