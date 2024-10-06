from model.Pessoas.Passageiros import Passageiro
from dao.DAOPassageiro import DAOPassageiro
from validate_docbr import CPF
import bcrypt

class ControladorPassageiro:
    def __init__(self):
        self.__dao = DAOPassageiro()
        self.passageiro_logado = None

    def set_passageiro_logado(self, passageiro):
        self.passageiro_logado = passageiro

    def cadastrar_passageiro(self, nome, cpf, data_nasc, senha, confirmar_senha):
        cpf_objeto = CPF()
        if not cpf_objeto.validate(cpf):
            raise ValueError("CPF Inválido")
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
            self.passageiro_logado.data_nascimento = nova_data_nasc
        if nova_senha:
            if nova_senha != confirmar_senha:
                return False, "As senhas não coincidem."
            self.passageiro_logado.senha = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt())

        if self.__dao.atualizar(self.passageiro_logado):
            return True, "Dados alterados com sucesso!"

        return False, "Erro ao alterar dados. Tente novamente."