from model.Pessoas.Pessoa import Pessoa

class Passageiro(Pessoa):
    contador = 0  # Variável de classe para contar instâncias

    def __init__(self, nome:str, cpf:str, senha:str, data_nascimento:str):
        # Incrementa o contador sempre que um novo passageiro é criado
        Passageiro.contador += 1
        # Define o código com base no contador
        cod = str(Passageiro.contador)  # Converte o contador para string
        super().__init__(cod, nome, cpf)  # Chama o construtor da classe pai
        self.__senha = senha
        self.__data_nascimento = data_nascimento

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        if isinstance(nova_senha, str):
            self.__senha = nova_senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if isinstance(nova_data, str):
            self.__data_nascimento = nova_data
