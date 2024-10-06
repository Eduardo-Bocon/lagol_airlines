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

"""from model.Pessoas.Pessoa import Pessoa

class Passageiro(Pessoa):
    contador = 0  # Variável de classe para contar instâncias

    def __init__(self, nome:str, cpf:str, senha:str, data_nascimento:str):
        # Incrementa o contador sempre que um novo passageiro é criado
        Passageiro.contador += 1
        # Define o código com base no contador
        cod = str(Passageiro.contador)  # Converte o contador para string
        super().__init__(cod, nome, cpf)  # Chama o construtor da classe pai
        self.__senha = senha
        self.__data_nascimento = data_nascimento

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if isinstance(nova_senha, str):
            self.__senha = nova_senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if isinstance(nova_data, str):
            self.__data_nascimento = nova_data
"""