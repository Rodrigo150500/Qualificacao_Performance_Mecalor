import json
import sys
import os

def abrirJson(filePath):
    with open(filePath, 'r') as json_file:
        return json.load(json_file)

def acharCaminhoComJson(devpath, buildPath):
    # Verifica se o programa está empacotado com PyInstaller ou rodando na IDE
    if getattr(sys, 'frozen', False):
        # Empacotado: a pasta de destino está no mesmo diretório do executável
        return os.path.abspath(os.path.join(os.path.dirname(sys.executable), devpath))
    else:
        # Executado na IDE: subindo dois níveis e acessando a pasta de destino
        return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{buildPath}'))

