import tkinter as tk
from tkinter import messagebox

class TelaFuncionarios(tk.Toplevel):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Gerenciar Funcionários")
        self.geometry("800x600")

        self.label = tk.Label(self, text="Funcionários", font=("Arial", 14))
        self.label.pack(pady=10)

        self.lista_funcionarios = tk.Listbox(self)
        self.lista_funcionarios.pack(expand=True, fill='both', padx=20, pady=10)

        self.adicionar_funcionario_button = tk.Button(self, text="Adicionar Funcionário", command=self.adicionar_funcionario)
        self.adicionar_funcionario_button.pack(pady=(20, 10))

        self.carregar_funcionarios()

    def carregar_funcionarios(self):
        funcionarios = self.controlador.controlador_funcionario.buscar_todos_funcionarios()
        if funcionarios:
            for funcionario in funcionarios:
                self.lista_funcionarios.insert(tk.END, f"{funcionario.nome}  ||  {funcionario.cargo}")
        else:
            messagebox.showinfo("Informação", "Nenhum funcionário cadastrado.")

    def adicionar_funcionario(self):
        from view.ViewCadastroFuncionario import TelaCadastroFuncionario
        TelaCadastroFuncionario(self.controlador)
