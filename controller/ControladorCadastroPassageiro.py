from model.ModeloCadastroPassageiro import PassageiroModel

class PassageiroController:
    def __init__(self, db_path):
        self.model = PassageiroModel(db_path)

    def cadastrar_passageiro(self, nome, idade, email):
        if nome and idade and email:
            self.model.adicionar_passageiro(nome, idade, email)
            return True
        return False

    def fechar(self):
        self.model.fechar_conexao()
