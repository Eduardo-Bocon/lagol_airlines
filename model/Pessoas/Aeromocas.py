from model.Pessoas.Funcionarios import Funcionario

class Aeromoca(Funcionario):
    def __init__(self, nome, cpf, treinamento):
        super().__init__(nome, cpf, "Aeromoça")
        self.__lotacao = []

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
        funcionario_dict = super().to_dict()
        funcionario_dict.update({
            "lotacao": self.__lotacao
        })
        return funcionario_dict
