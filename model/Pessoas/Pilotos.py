
from model.Pessoas import Funcionarios


class Piloto(Funcionarios):
    
    def __init__(self, cod: str, nome: str, cpf: str, cargo:str, lotacao:list):
        super().__init__(cod, nome, cpf, cargo, lotacao) 
        