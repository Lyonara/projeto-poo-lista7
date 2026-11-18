from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.categoria import Categoria
from models.categoriadao import CategoriaDAO
from models.produto import Produto
from models.produtodao import ProdutoDAO

class Service:
    # --- Cliente ---
    @staticmethod
    def cliente_inserir(nome, email, fone):
        ids = [c.get_id() for c in ClienteDAO().listar()]
        novo_id = max(ids) + 1 if ids else 1
        c = Cliente(novo_id, nome, email, fone)
        ClienteDAO().inserir(c)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    # --- Categoria ---
    @staticmethod
    def categoria_inserir(descricao):
        ids = [c.get_id() for c in CategoriaDAO().listar()]
        novo_id = max(ids) + 1 if ids else 1
        cat = Categoria(novo_id, descricao)
        CategoriaDAO().inserir(cat)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        cat = Categoria(id, descricao)
        CategoriaDAO().atualizar(cat)

    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO().excluir(id)

    # --- Produto ---
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        ids = [p.get_id() for p in ProdutoDAO().listar()]
        novo_id = max(ids) + 1 if ids else 1
        p = Produto(novo_id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().inserir(p)

    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        p = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().atualizar(p)

    @staticmethod
    def produto_excluir(id):
        ProdutoDAO().excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        for p in ProdutoDAO().listar():
            novo_preco = p.get_preco() * (1 + percentual / 100)
            p.set_preco(novo_preco)
            ProdutoDAO().atualizar(p)