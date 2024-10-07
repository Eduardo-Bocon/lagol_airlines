from Pessoas import Pessoas

class Admin(Pessoas):
    def __init__(self, nome, cpf, senha, is_admin):
        super().__init__(nome, cpf)
        self.__senha = None
        self.__is_admin = is_admin
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha  # Assume it's already hashed

    @property
    def is_admin(self):
        return self.__is_admin

    def to_dict(self):
        pessoa_dict = super().to_dict()
        pessoa_dict.update({
            "senha": self.__senha,
            "is_admin": self.__is_admin
        })
        return pessoa_dict