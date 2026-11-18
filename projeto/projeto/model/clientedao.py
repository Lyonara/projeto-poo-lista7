import json
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self._arquivo = "clientes.json"
        self._objetos = []
        self._abrir()

    def inserir(self, obj):
        self._objetos.append(obj)
        self._salvar()

    def listar(self):
        return self._objetos

    def listar_id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self._objetos.remove(aux)
            self._objetos.append(obj)
            self._salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self._objetos.remove(aux)
            self._salvar()

    def _abrir(self):
        try:
            arquivo = open(self._arquivo, mode="r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):
        arquivo = open(self._arquivo, mode="w")
        json.dump(self._objetos, arquivo, default=Cliente.to_json, indent=2)
        arquivo.close()