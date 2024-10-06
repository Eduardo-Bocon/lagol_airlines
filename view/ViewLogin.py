from view.ViewCadastroPassageiro import TelaCadastro
import tkinter as tk
from tkinter import messagebox

class TelaLogin(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        self.title("Tela de Login")
        self.geometry("800x600")

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.pack(pady=(20, 0))  # Adiciona espaço acima
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack(pady=(0, 10))  # Adiciona espaço abaixo

        self.senha_label = tk.Label(self, text="Senha:")
        self.senha_label.pack(pady=(20, 0))
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=(0, 10))

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=(10, 5))

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.abrir_cadastro)
        self.cadastrar_button.pack()

        # Botão para ir para a tela de login do admin
        self.admin_login_button = tk.Button(self, text="Login Admin", command=self.abrir_login_admin)
        self.admin_login_button.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)

    def login(self):
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()
        sucesso, mensagem = self.controlador.controlador_passageiro.validar_login(cpf, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
            from view.ViewPassageiro import TelaPassageiro
            TelaPassageiro(self.controlador)
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_cadastro(self):
        TelaCadastro(self.controlador)

    def abrir_login_admin(self):
        from view.ViewAdminLogin import TelaLoginAdmin
        self.destroy()
        TelaLoginAdmin(self.controlador)

