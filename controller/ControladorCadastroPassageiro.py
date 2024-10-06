from model.Pessoas.Cliente import Cliente
from view.ViewCadastroPassageiro import TelaCadastroPassageiro
from view.ViewLogin import TelaLogin  # Importe a tela de login
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class ControladorCadastroPassageiro:
    def __init__(self):
        self.tela = TelaCadastroPassageiro(self)
        self.cliente = None  # Atributo para armazenar a instância do cliente
        
    def cadastrar_passageiro(self, nome, cpf, senha, data_nascimento_str):
        # Verificar se todos os campos estão preenchidos
        if not nome or not cpf or not senha or not data_nascimento_str:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return

        # Converter a string da data para o formato de data
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Data Inválida", "Por favor, insira uma data válida no formato YYYY-MM-DD.")
            return

        # Criar uma instância do Cliente
        self.cliente = Cliente(cod=cpf, nome=nome, cpf=cpf, senha=senha, data_nascimento=data_nascimento)

        # Aqui você pode adicionar a lógica para salvar o passageiro em um banco de dados ou lista
        self.salvar_passageiro(self.cliente)

        messagebox.showinfo("Cadastro", "Passageiro cadastrado com sucesso!")

    def salvar_passageiro(self, cliente):
        # Implementar a lógica para salvar o passageiro (em um banco de dados, por exemplo)
        pass  # Substitua este pass pela lógica de persistência

    def retornar_login(self):
        # Fechar a tela de cadastro
        self.tela.janela.destroy()
        # Retornar para a tela de login
        TelaLogin(self).iniciar()  # Instanciar e iniciar a tela de login

    def iniciar(self):
        self.tela.iniciar()
