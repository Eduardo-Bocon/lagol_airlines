import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

class TelaCadastro(tk.Toplevel):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Tela de Cadastro")
        self.geometry("800x600")

        self.nome_label = tk.Label(self, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack()

        self.data_nasc_label = tk.Label(self, text="Data de Nascimento:")
        self.data_nasc_label.pack()
        self.data_nasc_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.data_nasc_entry.pack()

        self.senha_label = tk.Label(self, text="Senha:")
        self.senha_label.pack()
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.confirmar_senha_label = tk.Label(self, text="Confirmar Senha:")
        self.confirmar_senha_label.pack()
        self.confirmar_senha_entry = tk.Entry(self, show="*")
        self.confirmar_senha_entry.pack()

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack()

    def cadastrar(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        data_nasc = self.data_nasc_entry.get_date()
        senha = self.senha_entry.get()
        confirmar_senha = self.confirmar_senha_entry.get()

        sucesso, mensagem = self.controlador.controlador_passageiro.cadastrar_passageiro(nome, cpf, data_nasc, senha, confirmar_senha)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
        else:
            messagebox.showerror("Erro", mensagem)


"""import tkinter as tk
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
        self.janela.deiconify()  # Mostra a janela"""
