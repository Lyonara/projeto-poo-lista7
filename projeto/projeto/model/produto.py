class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self._id = id

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self._descricao = descricao

    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço deve ser positivo")
        self._preco = preco

    def set_estoque(self, estoque):
        if estoque < 0: raise ValueError("Estoque deve ser positivo")
        self._estoque = estoque

    def set_id_categoria(self, id_categoria):
        self._id_categoria = id_categoria

    def get_id(self): return self._id
    def get_descricao(self): return self._descricao
    def get_preco(self): return self._preco
    def get_estoque(self): return self._estoque
    def get_id_categoria(self): return self._id_categoria

    def __str__(self):
        return f"{self._id} - {self._descricao} - R$ {self._preco:.2f} - Estoque: {self._estoque} - Categoria ID: {self._id_categoria}"

    def to_json(self):
        return {
            "id": self._id,
            "descricao": self._descricao,
            "preco": self._preco,
            "estoque": self._estoque,
            "id_categoria": self._id_categoria
        }

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_categoria"])