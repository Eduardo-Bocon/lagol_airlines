from model.Pessoas.Pilotos import Piloto
from model.Pessoas.Aeromocas import Aeromoca
from dao.DAOFuncionario import DAOFuncionario
from validate_docbr import CPF

class ControladorFuncionario:
    def __init__(self):
        self.__dao = DAOFuncionario()

    def cadastrar_funcionario(self, nome, cpf, cargo):
        cpf_objeto = CPF()
        if not cpf_objeto.validate(cpf):
            raise ValueError("CPF Inválido")
        if self.__dao.buscar_por_cpf(cpf):
            return False, "Funcionário com esse CPF já cadastrado."

        if cargo == "Piloto":
            funcionario = Piloto(nome=nome, cpf=cpf)
        elif cargo == "Aeromoça":
            funcionario = Aeromoca(nome=nome, cpf=cpf)
        else:
            return False, "Cargo inválido."

        if self.__dao.adicionar(funcionario):
            return True, "Cadastro realizado com sucesso!"
        else:
            return False, "Erro ao cadastrar funcionário. Tente novamente."
