# view/ViewLogin.py
import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, controlador):
        self.controlador = controlador
        self.janela = tk.Tk()
        self.janela.title("Tela de Login")

        # Layout
        tk.Label(self.janela, text="Usuário:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_username = tk.Entry(self.janela)
        self.entry_username.pack(pady=5)

        tk.Label(self.janela, text="Senha:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_password = tk.Entry(self.janela, show='*')
        self.entry_password.pack(pady=5)

        self.botao_login = tk.Button(self.janela, text="Login", command=self.login)
        self.botao_login.pack(side=tk.LEFT, padx=20, pady=10)

        self.botao_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.pack(side=tk.LEFT, padx=20, pady=10)

        self.botao_sair = tk.Button(self.janela, text="Sair", command=self.sair, bg='red', fg='white')
        self.botao_sair.pack(side=tk.RIGHT, padx=20, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password:
            # Aqui você pode adicionar a lógica de login
            messagebox.showinfo("Login", f"Usuário {username} logado com sucesso!")
            self.janela.destroy()
        else:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

    def cadastrar(self):
        self.controlador.iniciar_cadastro_passageiro()  # Chama o controlador para abrir a tela de cadastro

    def sair(self):
        self.janela.destroy()

    def mostrar(self):
        self.janela.mainloop()
