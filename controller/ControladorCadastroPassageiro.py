# controller/ControladorCadastroPassageiro.py
from view.ViewCadastroPassageiro import TelaCadastroPassageiro

class ControladorCadastroPassageiro:
    def __init__(self):
        self.tela_cadastro_passageiro = TelaCadastroPassageiro(self)

    def cadastrar_passageiro(self, nome, cpf, senha, data_nascimento):
        # Implementar a lógica para armazenar os dados do passageiro
        print(f"Passageiro cadastrado: {nome}, CPF: {cpf}, Data de Nascimento: {data_nascimento}")

    def mostrar_tela_cadastro(self):
        self.tela_cadastro_passageiro.iniciar()  # Chama a função para iniciar a tela de cadastro
