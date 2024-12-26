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

x = VendaDAO.ler()

print(x[0].comprador)