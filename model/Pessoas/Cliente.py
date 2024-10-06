from datetime import date
from model.Pessoas.Pessoas import Pessoa  # Importando a classe Pessoa

class Cliente(Pessoa):
    
    def __init__(self, cod: str, nome: str, cpf: str, senha: str, data_nascimento: date):
        super().__init__(cod, nome, cpf)  # Chama o construtor da classe base Pessoa
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
        if isinstance(nova_data, date):
            self.__data_nascimento = nova_data
