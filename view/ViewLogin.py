from view.ViewCadastroPassageiro import TelaCadastro
import tkinter as tk
from tkinter import messagebox

class TelaLogin(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        self.title("Tela de Login")
        self.geometry("800x600")

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.pack(pady=(20, 0))  # Adiciona espaço acima
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack(pady=(0, 10))  # Adiciona espaço abaixo

        self.senha_label = tk.Label(self, text="Senha:")
        self.senha_label.pack(pady=(20, 0))
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=(0, 10))

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=(10, 5))

        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.abrir_cadastro)
        self.cadastrar_button.pack()

        # Botão para ir para a tela de login do admin
        self.admin_login_button = tk.Button(self, text="Login Admin", command=self.abrir_login_admin)
        self.admin_login_button.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)

    def login(self):
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()
        sucesso, mensagem = self.controlador.controlador_passageiro.validar_login(cpf, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.destroy()
            from view.ViewPassageiro import TelaPassageiro
            TelaPassageiro(self.controlador)
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_cadastro(self):
        TelaCadastro(self.controlador)

    def abrir_login_admin(self):
        from view.ViewAdminLogin import TelaLoginAdmin
        self.destroy()
        TelaLoginAdmin(self.controlador)



"""import tkinter as tk
from tkinter import messagebox

class TelaLogin:
    def __init__(self, controlador):
        self.controlador = controlador
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.janela.geometry("400x400")

        tk.Label(self.janela, text="Login", font=('Helvetica', 16, 'bold')).pack(pady=10)

        tk.Label(self.janela, text="CPF:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_cpf = tk.Entry(self.janela, font=('Helvetica', 12))
        self.entry_cpf.pack(pady=5)

        tk.Label(self.janela, text="Senha:", font=('Helvetica', 12)).pack(pady=5)
        self.entry_senha = tk.Entry(self.janela, show='*', font=('Helvetica', 12))
        self.entry_senha.pack(pady=5)

        self.botao_login = tk.Button(self.janela, text="Login", command=self.login, bg='green', fg='white', font=('Helvetica', 12))
        self.botao_login.pack(pady=20)

        self.botao_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.controlador.retornar_cadastro, bg='blue', fg='white', font=('Helvetica', 12))
        self.botao_cadastrar.pack(pady=5)

    def login(self):
        cpf = self.entry_cpf.get()
        senha = self.entry_senha.get()

        # Implementar a lógica para verificar o login
        if cpf == "123456789" and senha == "senha":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            # Aqui você pode direcionar para a tela principal
        else:
            messagebox.showwarning("Erro", "CPF ou Senha inválidos.")

    def iniciar(self):
        self.janela.deiconify()  # Mostra a janela
        self.janela.mainloop()
"""