import tkinter as tk
#from tkinter import messagebox

class TelaAdmin(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Tela Admin")
        self.geometry("800x600")

        self.voltar_button = tk.Button(self, text="Sair", command=self.voltar_para_login)
        self.voltar_button.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)

        self.funcionarios_button = tk.Button(self, text="Funcionários", command=self.gerenciar_funcionarios)
        self.funcionarios_button.pack(pady=(20, 5))

        self.avioes_button = tk.Button(self, text="Aviões", command=self.gerenciar_avioes)
        self.avioes_button.pack(pady=(20, 5))

        self.voos_button = tk.Button(self, text="Voos", command=self.gerenciar_voos)
        self.voos_button.pack(pady=(20, 5))

        self.tickets_button = tk.Button(self, text="Ver Tickets Emitidos", command=self.ver_tickets_emitidos)
        self.tickets_button.pack(pady=(20, 5))

    def voltar_para_login(self):
        self.destroy()
        from view.ViewLogin import TelaLogin
        TelaLogin(self.controlador)

    def gerenciar_funcionarios(self): #Adicionar redirecionamento aqui
        pass
    def gerenciar_avioes(self): #Adicionar redirecionamento aqui
        pass
    def gerenciar_voos(self): #Adicionar redirecionamento aqui
        pass
    def ver_tickets_emitidos(self):  #Adicionar redirecionamento aqui
        pass
