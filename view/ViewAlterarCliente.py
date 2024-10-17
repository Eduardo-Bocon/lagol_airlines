import PySimpleGUI as Sg

class TelaAlterarCliente:
    def __init__(self, controlador):
        self.controlador = controlador
        self.janela = None
        self.criar_janela()

    def criar_janela(self):
        layout = [
            [Sg.Push(), Sg.Text("Nome:"), Sg.InputText(key='nome'), Sg.Push()],
            [Sg.Push(), Sg.Text('Data de Nascimento:'), Sg.Input(key='data_nascimento'), Sg.CalendarButton('Data', target='data_nascimento', format='%d/%m/%Y'), Sg.Push()],
            [Sg.Push(), Sg.Text("Nova Senha (opcional):"), Sg.InputText(key='nova_senha', password_char='*'), Sg.Push()],
            [Sg.Push(), Sg.Text("Confirme a Nova Senha:"), Sg.InputText(key='confirma_nova_senha', password_char='*'), Sg.Push()],
            [Sg.Push(), Sg.Button("Salvar Alterações"), Sg.Button("Deletar Passageiro"), Sg.Button("Cancelar"), Sg.Push()]
        ]

        # Cria a janela
        self.janela = Sg.Window("Alterar Passageiro", layout, size=(400, 300))

    def abrir(self):
        while True:
            evento, valores = self.janela.read()

            if evento == Sg.WINDOW_CLOSED or evento == 'Cancelar':
                self.retornar_passageiro()
                break
            elif evento == 'Salvar Alterações':
                self.alterar_passageiro(valores)
            elif evento == 'Deletar Passageiro':
                self.deletar_passageiro()

        self.janela.close()

    def alterar_passageiro(self, valores):
        nome = valores['nome']
        data_nascimento = valores['data_nascimento']
        senha = valores['nova_senha']
        confirma_nova_senha = valores['confirma_nova_senha']

        sucesso, mensagem = self.controlador.controlador_passageiro.alterar_dados_passageiro(nome, data_nascimento, senha, confirma_nova_senha)

        if sucesso:
            Sg.popup("Sucesso", mensagem)
            self.janela.close()
            from view.ViewCliente import TelaCliente
            TelaCliente(self.controlador).abrir()
        else:
            Sg.popup("Erro", mensagem)

    def deletar_passageiro(self):
        resposta = Sg.popup_yes_no("Tem certeza que deseja deletar este passageiro?")
        if resposta == 'Yes':
            # Adicione a lógica de deletar passageiro aqui
            sucesso, mensagem = self.controlador.controlador_passageiro.deletar_passageiro()
            if sucesso:
                Sg.popup("Sucesso", mensagem)
                self.janela.close()
                from view.ViewLogin import TelaLogin  # Supondo que você quer voltar para a tela de login
                TelaLogin(self.controlador).abrir()
            else:
                Sg.popup("Erro", mensagem)

    def retornar_passageiro(self):
        self.janela.close()
        from view.ViewCliente import TelaCliente
        TelaCliente(self.controlador).abrir()
