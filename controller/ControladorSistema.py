from view.ViewLogin import TelaLogin
from view.ViewCadastroPassageiro import TelaCadastroPassageiro

class ControladorSistema:
    def __init__(self):
        self.janela_login = TelaLogin(self)  # Passa a referência do controlador
        self.janela_cadastro_passageiro = None  # Inicialmente sem a tela de cadastro

    def inicializa_sistema(self):
        self.janela_login.mostrar()  # Mostra a tela de login

    def abrir_cadastro(self):
        self.janela_login.janela.withdraw()  # Oculta a tela de login
        self.janela_cadastro_passageiro = TelaCadastroPassageiro(self)  # Cria a tela de cadastro
        self.janela_cadastro_passageiro.iniciar()  # Inicia a tela de cadastro

    def cadastrar_passageiro(self, nome, idade, documento):
        # Aqui você pode adicionar a lógica para cadastrar o passageiro
        print(f"Passageiro cadastrado: Nome: {nome}, Idade: {idade}, Documento: {documento}")

    def retornar_login(self):
        # Não é necessário, pois agora estamos chamando diretamente em `voltar()`.
        pass
