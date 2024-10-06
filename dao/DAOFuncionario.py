from dao.DAO import DAO
from model.Pessoas.Funcionarios import Funcionario

class DAOFuncionario(DAO):
    def __init__(self):
        super().__init__()
        self.__collection = self.db['funcionarios']

    def adicionar(self, funcionario):
        try:
            funcionario.cod = self.get_next_cod("funcionario_cod")
            result = self.__collection.insert_one(funcionario.to_dict())
            return result.inserted_id is not None
        except Exception as e:
            print(f"Erro ao adicionar funcionário: {e}")
            return False

    def buscar_por_cpf(self, cpf):
        funcionario_dict = self.__collection.find_one({"cpf": cpf})
        if funcionario_dict:
            return Funcionario(
                nome=funcionario_dict['nome'],
                cpf=funcionario_dict['cpf'],
                cargo=funcionario_dict['cargo'],
                senha=funcionario_dict['senha']
            )
        return None
