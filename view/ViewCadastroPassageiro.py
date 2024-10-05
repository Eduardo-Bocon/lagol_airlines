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

        tk.Label(self.janela, text="Idade:").grid(row=1, column=0)
        self.entry_idade = tk.Entry(self.janela)
        self.entry_idade.grid(row=1, column=1)

        tk.Label(self.janela, text="Documento:").grid(row=2, column=0)
        self.entry_documento = tk.Entry(self.janela)
        self.entry_documento.grid(row=2, column=1)

        self.botao_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.grid(row=3, columnspan=2)

        self.botao_voltar = tk.Button(self.janela, text="Voltar", command=self.voltar)
        self.botao_voltar.grid(row=4, columnspan=2)

    def cadastrar(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        documento = self.entry_documento.get()

        if not nome or not idade or not documento:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return

        self.controlador.cadastrar_passageiro(nome, idade, documento)
        messagebox.showinfo("Cadastro", "Passageiro cadastrado com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_documento.delete(0, tk.END)

    def voltar(self):
        self.janela.destroy()  # Fecha a tela de cadastro
        self.controlador.janela_login.janela.deiconify()  # Mostra a tela de login novamente

    def iniciar(self):
        self.janela.mainloop()
