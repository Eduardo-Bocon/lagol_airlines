from controller.ControladorPassageiro import ControladorPassageiro
from controller.ControladorAdminLogin import ControladorAdminLogin
from view.ViewLogin import TelaLogin

class ControladorSistema:
    def __init__(self):
        self.__controlador_passageiro = ControladorPassageiro()
        self.__controlador_admin_login = ControladorAdminLogin()

    @property
    def controlador_passageiro(self):
        return self.__controlador_passageiro

    @property
    def controlador_admin_login(self):
        return self.__controlador_admin_login

    def iniciar(self):
        app = TelaLogin(self)
        app.mainloop()



"""from view.ViewLogin import TelaLogin
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
"""