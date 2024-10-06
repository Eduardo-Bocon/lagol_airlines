import tkinter as tk
from tkinter import messagebox

class TelaCadastroPassageiro:
    def __init__(self, controlador):
        self.controlador = controlador
        self.janela = tk.Toplevel()  # Mudança para Toplevel
        self.janela.title("Cadastro de Passageiro")
        self.janela.geometry("400x400")
        self.janela.withdraw()  # Mantém a janela oculta até ser chamada

        tk.Label(self.janela, text="Cadastro de Passageiro", font=('Helvetica', 16, 'bold')).pack(pady=10)

        tk.Label(self.janela, text="Nome:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_nome = tk.Entry(self.janela, font=('Helvetica', 12))
        self.entry_nome.pack(pady=5)

        tk.Label(self.janela, text="CPF:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_cpf = tk.Entry(self.janela, font=('Helvetica', 12))
        self.entry_cpf.pack(pady=5)

        tk.Label(self.janela, text="Data de Nascimento:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_data_nascimento = tk.Entry(self.janela, font=('Helvetica', 12))
        self.entry_data_nascimento.pack(pady=5)

        tk.Label(self.janela, text="Senha:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_senha = tk.Entry(self.janela, show='*', font=('Helvetica', 12))
        self.entry_senha.pack(pady=5)

        tk.Label(self.janela, text="Confirmar Senha:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_confirmar_senha = tk.Entry(self.janela, show='*', font=('Helvetica', 12))
        self.entry_confirmar_senha.pack(pady=5)

        self.botao_cadastrar = tk.Button(self.janela, text="Avançar", command=self.cadastrar, bg='green', fg='white', font=('Helvetica', 12))
        self.botao_cadastrar.pack(pady=20)

        self.botao_login = tk.Button(self.janela, text="Login", command=self.voltar_login, bg='blue', fg='white', font=('Helvetica', 12))
        self.botao_login.pack(pady=5)

    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        data_nascimento = self.entry_data_nascimento.get()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        if not nome or not cpf or not data_nascimento or not senha or not confirmar_senha:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return
        
        if senha != confirmar_senha:
            messagebox.showwarning("Erro", "As senhas não coincidem.")
            return

        self.controlador.cadastrar_passageiro(nome, cpf, senha, data_nascimento)
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_confirmar_senha.delete(0, tk.END)

    def voltar_login(self):
        self.janela.withdraw()  # Oculta a tela de cadastro
        self.controlador.retornar_login()  # Retorna para a tela de login

    def iniciar(self):
        self.janela.deiconify()  # Mostra a janela
