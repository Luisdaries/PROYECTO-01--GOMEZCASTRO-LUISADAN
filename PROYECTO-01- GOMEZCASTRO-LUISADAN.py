# modulos a importar
import platform
import subprocess
import os
# validamos que el sistema operativo sea windows
if(platform.system() == 'Windows'):
    # el comando start en windows crea una nueva ventana prompt
    os.system("start \"test\" ./controller.py  ")
    # validamos que el sistema sea linux
if(platform.system() == 'Linux'):
        # el comando gnome-terminal ejecuta una nueva termina y se le pasa el command
    subprocess.Popen(["gnome-terminal", "-e", "python3 controller.py"])

