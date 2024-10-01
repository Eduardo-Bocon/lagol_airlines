# controller/controladorSistema.py

from controller.ControladorLogin import ControladorLogin

class ControladorSistema:
    def inicializa_sistema(self):
        controlador_login = ControladorLogin()
        controlador_login.realizar_login()

if __name__ == "__main__":
    ControladorSistema().inicializa_sistema()
