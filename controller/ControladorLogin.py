from view.ViewLogin import TelaLogin
from controller.ControladorCadastroPassageiro import ControladorCadastroPassageiro

class ControladorLogin:
    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.tela_login = TelaLogin(self)

    def iniciar(self):
        self.tela_login.iniciar()  # Chama o método iniciar da tela de login

    def retornar_cadastro(self):
        self.tela_login.janela.destroy()  # Fecha a tela de login
        controlador_cadastro = ControladorCadastroPassageiro()  # Cria uma nova instância do controlador de cadastro
        controlador_cadastro.iniciar()  # Inicia a tela de cadastro
