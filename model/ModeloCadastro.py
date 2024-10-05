# model/ModeloCadastro.py
import sqlite3

class ModeloCadastro:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS passageiros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    documento TEXT NOT NULL
                )
            ''')

    def cadastrar_passageiro(self, nome, idade, documento):
        with self.conn:
            self.conn.execute('''
                INSERT INTO passageiros (nome, idade, documento)
                VALUES (?, ?, ?)
            ''', (nome, idade, documento))

    def fechar_conexao(self):
        self.conn.close()
