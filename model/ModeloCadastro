# model/model.py

# model/model.py

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class ModeloCadastro:
    def __init__(self):
        self.pacientes = []
        self.funcionarios = []

    def cadastrar_paciente(self, nome, idade):
        self.pacientes.append(Paciente(nome, idade))

    def cadastrar_funcionario(self, nome, cargo):
        self.funcionarios.append(Funcionario(nome, cargo))

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ModeloLogin:
    def __init__(self):
        self.usuarios = {
            "usuario1": "senha1",
            "usuario2": "senha2"
        }

    def autenticar(self, username, password):
        return self.usuarios.get(username) == password
