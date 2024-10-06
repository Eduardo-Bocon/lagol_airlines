import tkinter as tk
#from tkinter import messagebox

class TelaPassageiro(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Tela do Passageiro")
        self.geometry("800x600")

        self.voltar_button = tk.Button(self, text="Sair", command=self.voltar_para_login)
        self.voltar_button.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)

        self.nova_reserva_button = tk.Button(self, text="Nova Reserva", command=self.nova_reserva)
        self.nova_reserva_button.pack(pady=(20, 5))

        self.minhas_reservas_button = tk.Button(self, text="Minhas Reservas", command=self.minhas_reservas)
        self.minhas_reservas_button.pack(pady=(20, 5))

        self.alterar_dados_button = tk.Button(self, text="Alterar Dados de Usuário", command=self.alterar_dados)
        self.alterar_dados_button.pack(pady=(20, 5))

    def voltar_para_login(self):
        self.destroy()
        from view.ViewLogin import TelaLogin
        TelaLogin(self.controlador)

    def nova_reserva(self):#Adicionar redirecionamento aqui
        pass

    def minhas_reservas(self):#Adicionar redirecionamento aqui
        pass

    def alterar_dados(self):#Adicionar redirecionamento aqui
        pass

