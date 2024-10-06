from view.ViewLogin import TelaLogin
from view.ViewCadastroPassageiro import TelaCadastroPassageiro

class ControladorSistema:
    def __init__(self):
        self.tela_login = TelaLogin(self)
        self.tela_cadastro = TelaCadastroPassageiro(self)

    def inicializa_sistema(self):
        self.tela_login.iniciar()  # Inicia apenas a tela de login

    def retornar_cadastro(self):
        self.tela_login.janela.withdraw()  # Oculta a tela de login
        self.tela_cadastro.iniciar()  # Inicia a tela de cadastro

    def retornar_login(self):
        self.tela_cadastro.janela.withdraw()  # Oculta a tela de cadastro
        self.tela_login.iniciar()  # Inicia a tela de login

    def cadastrar_passageiro(self, nome, cpf, senha, data_nascimento):
        # Implementar a lógica para cadastrar o passageiro
        pass  # Substitua pelo código de persistência
