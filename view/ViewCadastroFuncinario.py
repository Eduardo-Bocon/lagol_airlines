import tkinter as tk
from tkinter import messagebox

class TelaCadastrarFuncionario(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Cadastrar Funcionário")
        self.geometry("400x300")

        tk.Label(self, text="Nome:").pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        tk.Label(self, text="CPF:").pack()
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack()

        tk.Label(self, text="Cargo:").pack()
        self.cargo_entry = tk.Entry(self)
        self.cargo_entry.pack()

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.cadastrar_funcionario)
        self.cadastrar_button.pack(pady=20)

    def cadastrar_funcionario(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        cargo = self.cargo_entry.get()

        sucesso, mensagem = self.controlador.cadastrar_funcionario(nome, cpf, cargo)

        if sucesso:
            tk.messagebox.showinfo("Sucesso", mensagem)
        else:
            tk.messagebox.showerror("Erro", mensagem)
