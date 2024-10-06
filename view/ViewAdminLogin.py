import tkinter as tk
from tkinter import messagebox

class TelaLoginAdmin(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Tela de Login Admin")
        self.geometry("800x600")

        self.cpf_label = tk.Label(self, text="CPF Admin:")
        self.cpf_label.pack(pady=(20, 0))  # Adiciona espaço acima
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack(pady=(0, 10))  # Adiciona espaço abaixo

        self.senha_label = tk.Label(self, text="Senha Admin:")
        self.senha_label.pack(pady=(20, 0))  # Adiciona espaço acima
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=(0, 20))  # Adiciona espaço abaixo

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=(10, 5))  # Adiciona espaço abaixo

        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar_para_login_passageiro)
        self.voltar_button.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)

    def login(self):
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()

        sucesso, mensagem = self.controlador.controlador_admin_login.validar_login_admin(cpf, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.abrir_tela_principal_admin()
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_tela_principal_admin(self):
        self.destroy()
        from view.ViewAdmin import TelaAdmin
        TelaAdmin(self.controlador)

    def voltar_para_login_passageiro(self):
        self.destroy()
        from view.ViewLogin import TelaLogin
        TelaLogin(self.controlador)
