import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

class TelaCadastroFuncionarios(tk.Toplevel):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Tela de Cadastro de Funcionários")
        self.geometry("800x600")

        self.nome_label = tk.Label(self, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack()

        self.cargo_var = tk.StringVar()
        self.piloto_radio = tk.Radiobutton(self, text="Piloto", variable=self.cargo_var, value="Piloto")
        self.piloto_radio.pack()
        self.aeromoça_radio = tk.Radiobutton(self, text="Aeromoça(o)", variable=self.cargo_var, value="Aeromoça(o)")
        self.aeromoça_radio.pack()

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack()
        self.cancelar_button = tk.Button(self, text="Cancelar", command=self.destroy)
        self.cancelar_button.pack()

    def cadastrar(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        cargo = self.cargo_var.get()

        if self.controlador.cadastrar_funcionario(nome, cpf, cargo):
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
            self.destroy()
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar funcionário. Verifique os dados e tente novamente.")