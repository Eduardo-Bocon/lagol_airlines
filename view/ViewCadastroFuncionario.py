import tkinter as tk
from tkinter import messagebox

class TelaCadastroFuncionario(tk.Tk):
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
        self.cargo_var = tk.StringVar(value="Piloto")  # Valor padrão

        # Colocando os Radiobuttons lado a lado
        self.piloto_radio = tk.Radiobutton(self, text="Piloto", variable=self.cargo_var, value="Piloto")
        self.piloto_radio.pack(side=tk.LEFT)

        self.aeromoça_radio = tk.Radiobutton(self, text="Aeromoça", variable=self.cargo_var, value="Aeromoça")
        self.aeromoça_radio.pack(side=tk.LEFT)

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.cadastrar_funcionario)
        self.cadastrar_button.pack(pady=20)

    def cadastrar_funcionario(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        cargo = self.cargo_var.get()  # Obter o valor do cargo selecionado

        sucesso, mensagem = self.controlador.controlador_funcionario.cadastrar_funcionario(nome, cpf, cargo)

        if sucesso:
            tk.messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
            from view.ViewFuncionarios import TelaFuncionarios
            TelaFuncionarios(self.controlador)
        else:
            tk.messagebox.showerror("Erro", mensagem)

