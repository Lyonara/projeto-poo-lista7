class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self._id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self._nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self._email = email

    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self._fone = fone

    def get_id(self): return self._id
    def get_nome(self): return self._nome
    def get_email(self): return self._email
    def get_fone(self): return self._fone

    def __str__(self):
        return f"{self._id} - {self._nome} - {self._email} - {self._fone}"

    def to_json(self):
        return { "id": self._id, "nome": self._nome, "email": self._email, "fone": self._fone }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])