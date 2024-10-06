import tkinter as tk
from tkinter import messagebox

class TelaAlterarFuncionario(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Alterar Funcionário")
        self.geometry("400x300")

        tk.Label(self, text="Nome:").pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        tk.Label(self, text="CPF:").pack()
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack()

        self.salvar_button = tk.Button(self, text="Salvar Alterações", command=self.alterar_funcionario)
        self.salvar_button.pack(pady=20)

    def alterar_funcionario(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()

        sucesso, mensagem = self.controlador.alterar_funcionario(nome, cpf)

        if sucesso:
            tk.messagebox.showinfo("Sucesso", mensagem)
        else:
            tk.messagebox.showerror("Erro", mensagem)
