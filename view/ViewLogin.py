import tkinter as tk
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
