# view/ViewCadastroPassageiro.py
import tkinter as tk
from tkinter import messagebox

class TelaCadastroPassageiro:
    def __init__(self, controlador):
        self.controlador = controlador
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Passageiro")

        tk.Label(self.janela, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self.janela, text="CPF:").grid(row=1, column=0)
        self.entry_cpf = tk.Entry(self.janela)
        self.entry_cpf.grid(row=1, column=1)

        tk.Label(self.janela, text="Senha:").grid(row=2, column=0)
        self.entry_senha = tk.Entry(self.janela, show='*')
        self.entry_senha.grid(row=2, column=1)

        tk.Label(self.janela, text="Data de Nascimento:").grid(row=3, column=0)
        self.entry_data_nascimento = tk.Entry(self.janela)
        self.entry_data_nascimento.grid(row=3, column=1)

        self.botao_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.grid(row=4, columnspan=2)

    def cadastrar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        senha = self.entry_senha.get()
        data_nascimento = self.entry_data_nascimento.get()

        if not nome or not cpf or not senha or not data_nascimento:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return

        self.controlador.cadastrar_passageiro(nome, cpf, senha, data_nascimento)
        messagebox.showinfo("Cadastro", "Passageiro cadastrado com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)

    def iniciar(self):
        self.janela.mainloop()
