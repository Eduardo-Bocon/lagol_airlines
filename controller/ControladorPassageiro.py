from model.Pessoas.Passageiros import Passageiro
from dao.DAOPassageiro import DAOPassageiro
from validate_docbr import CPF
import bcrypt
from datetime import datetime


class ControladorPassageiro:
    def __init__(self):
        self.__dao = DAOPassageiro()
        self.passageiro_logado = None

    def set_passageiro_logado(self, passageiro):
        self.passageiro_logado = passageiro

    def calcular_idade(self, data_nasc_str):
        data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade

    def cadastrar_passageiro(self, nome, cpf, data_nasc, senha, confirmar_senha):
        cpf_objeto = CPF()

        if not cpf_objeto.validate(cpf):
            raise ValueError("CPF Inválido")

        idade = self.calcular_idade(data_nasc)
        if idade < 18:
            return False, "Somente maiores de 18 anos podem se cadastrar."

        if senha != confirmar_senha:
            return False, "As senhas não coincidem."

        if self.__dao.buscar_por_cpf(cpf):
            return False, "Passageiro com esse CPF já cadastrado."

        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        passageiro = Passageiro(nome=nome, cpf=cpf, data_nascimento=data_nasc, senha=hashed_senha)

        if self.__dao.adicionar(passageiro):
            return True, "Cadastro realizado com sucesso!"
        else:
            return False, "Erro ao cadastrar passageiro. Tente novamente."

    def validar_login(self, cpf, senha):
        passageiro = self.__dao.buscar_por_cpf(cpf)
        if not passageiro:
            return False, "Passageiro não encontrado."
        if bcrypt.checkpw(senha.encode('utf-8'), passageiro.senha):
            self.set_passageiro_logado(passageiro)
            return True, "Login realizado com sucesso!"
        return False, "Senha incorreta."

    def alterar_dados_passageiro(self, novo_nome=None, nova_data_nasc=None, nova_senha=None, confirmar_senha=None):
        if not self.passageiro_logado:
            return False, "Nenhum passageiro logado."

        if novo_nome:
            self.passageiro_logado.nome = novo_nome

        if nova_data_nasc:
            idade = self.calcular_idade(nova_data_nasc)
            if idade < 18:
                return False, "Somente maiores de 18 anos podem alterar a data de nascimento para essa nova data."
            self.passageiro_logado.data_nascimento = nova_data_nasc

        if nova_senha:
            if nova_senha != confirmar_senha:
                return False, "As senhas não coincidem."
            self.passageiro_logado.senha = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt())

        if self.__dao.atualizar(self.passageiro_logado):
            return True, "Dados alterados com sucesso!"
        else:
            return False, "Erro ao alterar dados. Tente novamente."
