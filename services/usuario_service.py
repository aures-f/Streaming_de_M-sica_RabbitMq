import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from messaging import consume

historico = []

def registrar(event):
    historico.append(event)
    print('Histórico atualizado:', historico)

consume('historico', registrar)
