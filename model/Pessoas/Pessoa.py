from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, cod:str, nome:str, cpf:str):
        self.__cod = cod
        self.__nome = nome
        self.__cpf = cpf

    @property
    def cod(self):
        return self.__cod
    
    @cod.setter
    def cod(self, novo_cod):
        if isinstance(novo_cod, str):
            self.__cod = novo_cod

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str):
            self.__cpf = novo_cpf
