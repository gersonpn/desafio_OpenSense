import pandas as pd
import os

pasta = "D:\\Documents\\teste_open_sense\\PATENTES"

arquivos = os.listdir(pasta)

# alteração do nome dos arquivos conforme solicitação do teste
for numero, item in enumerate(arquivos, start=1):
    caminho = os.path.join(pasta,item)
    alteracao = os.path.splitext(item)[1]
    nome = f"Arq{numero}{alteracao}"
    nova_alteracao = os.path.join(pasta, nome)
    os.rename(caminho, nova_alteracao)
