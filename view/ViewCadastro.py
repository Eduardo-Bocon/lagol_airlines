# view/ViewCadastro.py

import PySimpleGUI as sg

class TelaCadastroPaciente:
    def __init__(self):
        self.layout = [
            [sg.Text("Cadastro de Paciente", font=('Helvetica', 14, 'bold'))],
            [sg.Text("Nome do Paciente:", font=('Helvetica', 12)), sg.InputText(key='nome')],
            [sg.Text("Idade:", font=('Helvetica', 12)), sg.InputText(key='idade')],
            [sg.Button("Cadastrar"), sg.Button("Voltar", button_color='red')]
        ]
        self.window = sg.Window("Cadastro de Paciente", self.layout, element_justification='c')

    def mostrar(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == "Voltar":
                return None, None

            if event == "Cadastrar":
                return values['nome'], values['idade']

        self.window.close()


class TelaCadastroFuncionario:
    def __init__(self):
        self.layout = [
            [sg.Text("Cadastro de Funcionário", font=('Helvetica', 14, 'bold'))],
            [sg.Text("Nome do Funcionário:", font=('Helvetica', 12)), sg.InputText(key='nome')],
            [sg.Text("Cargo:", font=('Helvetica', 12)), sg.InputText(key='cargo')],
            [sg.Button("Cadastrar"), sg.Button("Voltar", button_color='red')]
        ]
        self.window = sg.Window("Cadastro de Funcionário", self.layout, element_justification='c')

    def mostrar(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == "Voltar":
                return None, None

            if event == "Cadastrar":
                return values['nome'], values['cargo']

        self.window.close()
