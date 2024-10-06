from model.ModeloLogin import ModeloCadastro
from view.ViewCadastro import TelaCadastroPaciente, TelaCadastroFuncionario
import PySimpleGUI as sg

class ControladorCadastro:
    def __init__(self):
        self.modelo = ModeloCadastro()

    def cadastrar_paciente(self):
        tela = TelaCadastroPaciente()
        while True:
            nome, idade = tela.mostrar()
            if nome is None or idade is None:
                break

            self.modelo.cadastrar_paciente(nome, idade)
            sg.popup(f"Paciente {nome} cadastrado com sucesso!")

    def cadastrar_funcionario(self):
        tela = TelaCadastroFuncionario()
        while True:
            nome, cargo = tela.mostrar()
            if nome is None or cargo is None:
                break

            self.modelo.cadastrar_funcionario(nome, cargo)
            sg.popup(f"Funcionário {nome} cadastrado com sucesso!")
