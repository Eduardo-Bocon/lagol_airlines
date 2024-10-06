from dao.DAO import DAO
from model.Pessoas.Passageiros import Passageiro


class DAOPassageiro(DAO):
    def __init__(self):
        super().__init__()
        self.__collection = self.db['passageiros']

    def adicionar(self, passageiro):
        try:
            passageiro.cod = self.get_next_cod("passageiro_cod")
            result = self.__collection.insert_one(passageiro.to_dict())
            return result.inserted_id is not None
        except Exception as e:
            print(f"Erro ao adicionar passageiro: {e}")
            return False

    def buscar_por_cpf(self, cpf):
        passageiro_dict = self.__collection.find_one({"cpf": cpf})

        if passageiro_dict:
            return Passageiro(
                nome=passageiro_dict['nome'],
                cpf=passageiro_dict['cpf'],
                data_nascimento=passageiro_dict['data_nascimento'],
                senha=passageiro_dict['senha']
            )
        return None
