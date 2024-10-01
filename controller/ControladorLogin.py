from model.ModeloLogin import ModeloCadastro
from view.ViewCadastro import TelaCadastroPaciente, TelaCadastroFuncionario
from view.view import TelaLogin
from controller.controladorCadastro import ControladorCadastro
import PySimpleGUI as sg

class ControladorLogin:
    def __init__(self):
        self.modelo = ModeloCadastro()
        self.tela = TelaLogin()

    def realizar_login(self):
        while True:
            username, password = self.tela.mostrar()
            if username is None or password is None:
                break

            if username == "admin" and password == "admin":
                sg.popup("Login bem-sucedido! Você está no sistema.")
                break
            elif self.modelo.autenticar(username, password):
                sg.popup("Login bem-sucedido!")
                break
            else:
                sg.popup("Usuário ou senha incorretos!")

            # Adicionando a opção de cadastro
            if username == "cadastrar":
                self.abrir_cadastro()

    def abrir_cadastro(self):
        controlador_cadastro = ControladorCadastro()
        controlador_cadastro.cadastrar_paciente()
        controlador_cadastro.cadastrar_funcionario()
