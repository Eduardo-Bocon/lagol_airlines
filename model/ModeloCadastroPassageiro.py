import sqlite3

class PassageiroModel:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conexao = sqlite3.connect(self.db_path)
        self.cursor = self.conexao.cursor()
        
        # Criar tabela se não existir
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS passageiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL
        )
        ''')
        self.conexao.commit()

    def adicionar_passageiro(self, nome, idade, email):
        self.cursor.execute('''INSERT INTO passageiros (nome, idade, email) VALUES (?, ?, ?)''', (nome, idade, email))
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
