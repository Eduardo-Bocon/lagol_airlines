# view/view.py

import PySimpleGUI as sg

class TelaLogin:
    def __init__(self):
        self.layout = [
            [sg.Text("Usuário:", font=('Helvetica', 12)), sg.InputText(key='username')],
            [sg.Text("Senha:", font=('Helvetica', 12)), sg.InputText(key='password', password_char='*')],
            [sg.Button("Login"), sg.Button("Cadastrar"), sg.Button("Sair")]
        ]
        self.window = sg.Window("Tela de Login", self.layout, element_justification='c')

    def mostrar(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == "Sair":
                return None, None

            if event == "Login":
                return values['username'], values['password']

            if event == "Cadastrar":
                return "cadastrar", None

        self.window.close()
