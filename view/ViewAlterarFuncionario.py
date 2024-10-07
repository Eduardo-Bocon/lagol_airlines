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

        self.salvar_button = tk.Button(self, text="Salvar Alterações", command=self.alterar_funcionario)
        self.salvar_button.pack(pady=20)

        self.salvar_button = tk.Button(self, text="Cancelar", command=self.retornar_funcionario)
        self.salvar_button.pack(pady=20)

    def alterar_funcionario(self):
        nome = self.nome_entry.get()

        sucesso, mensagem = self.controlador.controlador_funcionario.alterar_funcionario(self, nome)

        if sucesso:
            tk.messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
            from view.ViewFuncionarios import TelaFuncionarios
            TelaFuncionarios(self.controlador)
        else:
            tk.messagebox.showerror("Erro", mensagem)

    def retornar_funcionario(self):
        self.destroy()
        from view.ViewFuncionarios import TelaFuncionarios
        TelaFuncionarios(self.controlador)
