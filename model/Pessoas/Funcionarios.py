from model.Pessoas.Pessoas import Pessoa  

class Funcionarios(Pessoa):
    
    def __init__(self, cod: str, nome: str, cpf: str, cargo:str, lotacao:list):
        super().__init__(cod, nome, cpf)
        self.__cargo = cargo
        self.__lotacao = lotacao

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, nova_cargo):
        if isinstance(nova_cargo, str):
            self.__cargo = nova_cargo

    @property
    def lotacao(self):
        return self.__lotacao
    
    @lotacao.setter
    def lotacao(self, nova_lotacao):
        if isinstance(nova_lotacao, str):
            self.__lotacao = nova_lotacao

    