# controller/ControladorSistema.py
from view.ViewLogin import TelaLogin
from controller.ControladorCadastroPassageiro import ControladorCadastroPassageiro

class ControladorSistema:
    def __init__(self):
        self.tela_login = TelaLogin(self)

    def iniciar_cadastro_passageiro(self):
        self.tela_login.janela.destroy()  # Fecha a tela de login
        controlador_cadastro = ControladorCadastroPassageiro()  # Cria um novo controlador
        controlador_cadastro.mostrar_tela_cadastro()  # Mostra a tela de cadastro

    def inicializa_sistema(self):
        self.tela_login.mostrar()
