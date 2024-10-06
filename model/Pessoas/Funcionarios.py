from model.Pessoas.Pessoas import Pessoas

class Funcionario(Pessoas):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__lotacao = []  # Inicializa uma lista vazia para armazenar os voos

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    @property
    def lotacao(self):
        return self.__lotacao

    def adicionar_voo(self, voo):
        if voo not in self.__lotacao:
            self.__lotacao.append(voo)

    def remover_voo(self, voo):
        if voo in self.__lotacao:
            self.__lotacao.remove(voo)

    def to_dict(self):
        pessoa_dict = super().to_dict()
        pessoa_dict.update({
            "cargo": self.__cargo,
            "lotacao": self.__lotacao
        })
        return pessoa_dict
