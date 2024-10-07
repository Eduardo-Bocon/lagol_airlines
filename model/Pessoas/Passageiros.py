from model.Pessoas.Pessoas import Pessoas
from datetime import date, datetime


class Passageiro(Pessoas):
    def __init__(self, nome, cpf, data_nascimento, senha):
        super().__init__(nome, cpf)
        self.__data_nascimento = None
        self.__senha = None
        self.data_nascimento = data_nascimento
        self.senha = senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if isinstance(nova_data, datetime):
            self.__data_nascimento = nova_data

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha  # Assume it's already hashed

    def to_dict(self):
        pessoa_dict = super().to_dict()
        pessoa_dict.update({
            "data_nascimento": self.__data_nascimento,
            "senha": self.__senha
        })
        return pessoa_dict
