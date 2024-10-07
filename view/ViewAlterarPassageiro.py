import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Importe o DateEntry

class TelaAlterarPassageiro(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Alterar Passageiro")
        self.geometry("400x300")

        tk.Label(self, text="Nome:").pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.data_nasc_label = tk.Label(self, text="Data de Nascimento:")
        self.data_nasc_label.pack()
        self.data_nasc_entry = DateEntry(self, date_pattern='dd/mm/yyyy', width=12, background='darkblue', foreground='white', borderwidth=2)
        self.data_nasc_entry.pack()

        tk.Label(self, text="Nova Senha (opcional):").pack()
        self.nova_senha_entry = tk.Entry(self, show='*')
        self.nova_senha_entry.pack()

        tk.Label(self, text="Confirme a Nova Senha:").pack()
        self.confirma_nova_senha_entry = tk.Entry(self, show='*')
        self.confirma_nova_senha_entry.pack()

        self.salvar_button = tk.Button(self, text="Salvar Alterações", command=self.alterar_passageiro)
        self.salvar_button.pack(pady=20)

        self.salvar_button = tk.Button(self, text="Cancelar", command=self.retornar_passageiro)
        self.salvar_button.pack(pady=20)

    def alterar_passageiro(self):
        nome = self.nome_entry.get()
        data_nascimento = self.data_nasc_entry.get()
        senha = self.nova_senha_entry.get()
        confirma_nova_senha = self.confirma_nova_senha_entry.get()

        sucesso, mensagem = self.controlador.controlador_passageiro.alterar_dados_passageiro(nome, data_nascimento, senha, confirma_nova_senha)

        if sucesso:
            tk.messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
            from view.ViewPassageiro import TelaPassageiro
            TelaPassageiro(self.controlador)
        else:
            tk.messagebox.showerror("Erro", mensagem)

    def retornar_passageiro(self):
        self.destroy()
        from view.ViewPassageiro import TelaPassageiro
        TelaPassageiro(self.controlador)
