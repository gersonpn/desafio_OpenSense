import pandas as pd
import re
import os
from bs4 import BeautifulSoup

pasta = "D:\\Documents\\teste_open_sense\\PATENTES"

arquivos = os.listdir(pasta)

# alteração do nome dos arquivos conforme solicitação do teste
if any(not arquivo.lower().startswith("arq") for arquivo in arquivos):
  for numero, item in enumerate(arquivos, start=1):
      caminho = os.path.join(pasta,item)
      alteracao = os.path.splitext(item)[1]
      nome = f"Arq{numero}{alteracao}"
      nova_alteracao = os.path.join(pasta, nome)
      os.rename(caminho, nova_alteracao)


# extração das informações de dentro do arquivo
def informacoes(arquivo):
    with open(arquivo, 'r', encoding='utf-8', errors='ignore') as arq:
      soup = BeautifulSoup(arq, 'html.parser')
      texto_arquivo = soup.get_text()
      verificacao_cnpj = r'\d{14}'
      cnpj = re.findall(verificacao_cnpj, texto_arquivo)
      resultado = len(cnpj)
      return cnpj, resultado

for elementos in arquivos:
    caminho_arquivo = os.path.join(pasta, elementos)
    cnpjs = informacoes(caminho_arquivo)
    resultado = informacoes(caminho_arquivo)
    print(f"itens {elementos}: {cnpjs}")