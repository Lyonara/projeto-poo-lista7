class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self._id = id

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self._descricao = descricao

    def get_id(self): return self._id
    def get_descricao(self): return self._descricao

    def __str__(self):
        return f"{self._id} - {self._descricao}"

    def to_json(self):
        return { "id": self._id, "descricao": self._descricao }

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])