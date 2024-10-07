from dao.DAOAdminLogin import DAOAdminLogin
import bcrypt

class ControladorAdminLogin:
    def __init__(self):
        self.__dao = DAOAdminLogin()

    def validar_login_admin(self, cpf, senha):
        admin = self.__dao.buscar_por_cpf(cpf)
        print(admin['cpf'])
        if admin and admin['is_admin'] is True:
            print(senha)
            if bcrypt.checkpw(senha.encode('utf-8'), admin['senha']):
                return True, "Login realizado com sucesso!"
        return False, "CPF ou senha inválidos."
