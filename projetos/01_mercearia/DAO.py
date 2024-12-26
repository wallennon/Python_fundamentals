from Models import *

class CategoriaDAO:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        lista_categoria = []
        for i in cls.categoria:
            lista_categoria.append(Categoria(i))
        
        return lista_categoria

class VendaDAO:
    @classmethod
    def salvar(cls, venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(f'{venda.itemVendido.nome} | {venda.itemVendido.preco} | {venda.itemVendido.categoria} | {venda.vendedor} | {venda.comprador} | {str(venda.quantidadeVendida)} | {venda.data}\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        lista_venda = []
        for i in cls.venda:
            lista_venda.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        
        return lista_venda
    # VendaDAO.salvar(Venda(Produtos('Arroz', 10, 'Alimento'), 'Germano', 'Cliente', 2))
    # VendaDAO.salvar(Venda(Produtos('Feijão', 8, 'Alimento'), 'Germano', 'Cliente', 1))
    # x = VendaDAO.ler()
    # print(x[0].comprador)

class EstoqueDAO:
    @classmethod
    def salvar(cls, produto:Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(f'{produto.nome} | {produto.preco} | {produto.categoria} | {str(quantidade)}\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        lista_estoque = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                lista_estoque.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))

        return lista_estoque
    # EstoqueDAO.salvar(Produtos('Feijão', 12, 'Alimento'), 25)
    # x = EstoqueDAO.ler()
    # print(f'Produto: {x[1].produto.nome} | Quantidade: {x[1].quantidade}')

class FornecedorDAO:
    @classmethod
    def salvar(cls, fornecedor:Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(f'{fornecedor.nome} | {fornecedor.cnpj} | {fornecedor.telefone} | {fornecedor.categoria}\n')
        
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        lista_fornecedor = []
        for i in cls.fornecedor:
            lista_fornecedor.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return lista_fornecedor
    # FornecedorDAO.salvar(Fornecedor('Vitor', '123456789', '987654321', 'Alimento'))
    # x = FornecedorDAO.ler()
    # print(f'Nome: {x[0].nome} | CNPJ: {x[0].cnpj} | Telefone: {x[0].telefone} | Categoria: {x[0].categoria}')

class PessoaDAO:
    @classmethod
    def salvar(cls, pessoa:Pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.writelines(f'{pessoa.nome} | {pessoa.telefone} | {pessoa.cpf} | {pessoa.email} | {pessoa.endereco}\n')
    
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        lista_pessoa = []
        for i in cls.pessoa:
            lista_pessoa.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        
        return lista_pessoa

class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario:Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(f'{funcionario.clt} | {int(funcionario.salario)} | {funcionario.cargo} | {funcionario.nome} | {funcionario.telefone} | {funcionario.cpf} | {funcionario.email} | {funcionario.endereco}\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        lista_funcionario = []
        for i in cls.funcionario:
            lista_funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        
        return lista_funcionario